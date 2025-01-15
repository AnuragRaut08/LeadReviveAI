import twilio from "twilio";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { lead } = req.body;

  if (!lead) {
    return res.status(400).json({ error: "Lead phone number is required" });
  }

  const accountSid = process.env.TWILIO_ACCOUNT_SID;
  const authToken = process.env.TWILIO_AUTH_TOKEN;
  const twilioNumber = process.env.TWILIO_PHONE_NUMBER;

  try {
    const client = twilio(accountSid, authToken);

    const call = await client.calls.create({
      to: lead,
      from: twilioNumber,
      url: "https://handler.twilio.com/twiml/EHXXXXXXXXXXXXXXXXXXXXXXXXXX", // Replace with Twilio Studio Flow URL
    });

    res.status(200).json({ message: "Call initiated successfully", callSid: call.sid });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
