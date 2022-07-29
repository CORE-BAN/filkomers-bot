from discord import Webhook, RequestsWebhookAdapter


def send_message(TEXT, WEBHOOK_DISCORD):
    CLIENT_ID = WEBHOOK_DISCORD[8:].split("/")[3]
    WEBHOOK_URL = WEBHOOK_DISCORD[8:].split("/")[4]
    webhook = Webhook.partial(CLIENT_ID, WEBHOOK_URL,
                              adapter=RequestsWebhookAdapter())
    webhook.send(content=TEXT)
