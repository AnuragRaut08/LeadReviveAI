import os
import time
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from src.base.leads_loader.airtable import AirtableLeadLoader
from src.vapi_automation import VapiAutomation
from src.groclake.modellake import analyze_sentiment
from src.utils.logger import setup_logger

# Load .env file
load_dotenv()

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Initialize logger
logger = setup_logger('LeadReviveAI', 'leadreviveai.log')

# Initialize leads loader (Airtable, Sheets, Hubspot or add your own custom CRM)
lead_loader = AirtableLeadLoader(
    access_token=os.getenv("AIRTABLE_ACCESS_TOKEN"),
    base_id=os.getenv("AIRTABLE_BASE_ID"),
    table_name=os.getenv("AIRTABLE_TABLE_NAME"),
)

# Get Vapi automation instance
automation = VapiAutomation(lead_loader)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.post("/execute")
async def execute(payload: dict):
    """
    Trigger the lead processing workflow. Payload should contain list of lead IDs.
    """
    try:
        lead_ids = payload.get("lead_ids", [])
        logger.info("Fetching lead data...")
        leads = automation.load_leads(lead_ids=lead_ids)
        if not leads:
            return {"message": "No leads found."}

        for lead in leads:
            automation.pre_call_processing(lead)
            call_params = automation.get_call_input_params(lead)
            logger.info(f"Call Inputs:\n {call_params}")
            logger.info(f"Calling Lead {lead.id}...")
            output = await automation.make_call(call_params)
            time.sleep(1)

        return {"message": "Calls initiated successfully for all leads."}
    except ValueError as e:
        logger.error(f"ValueError: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while executing the workflow")

@app.post("/webhook")
async def handle_webhook(request: Request):
    """
    Handle incoming webhook requests from Vapi.
    """
    try:
        response = await automation.handle_webhook_call(request)
        return response
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid webhook payload")

@app.post("/analyze_sentiment")
async def analyze_text_sentiment(payload: dict):
    """
    Analyze sentiment of a given text.
    """
    try:
        text = payload.get("text", "")
        if not text:
            raise ValueError("Text input is required")
        sentiment_score, sentiment_label = analyze_sentiment(text)
        logger.info(f"Sentiment: {sentiment_label} (Score: {sentiment_score})")
        return {"sentiment": sentiment_label, "score": sentiment_score}
    except ValueError as e:
        logger.error(f"ValueError: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while analyzing sentiment")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
