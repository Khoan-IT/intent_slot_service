import os
import sys
import json

import grpc
import intent_slot_service_pb2
import intent_slot_service_pb2_grpc

from underthesea import word_tokenize

MONITOR_SERVER_INTERFACE = os.environ.get('HOST', 'localhost')
MONITOR_SERVER_PORT = int(os.environ.get('PORT', 8000))

CHANNEL_IP = f"{MONITOR_SERVER_INTERFACE}:{MONITOR_SERVER_PORT}"

def main():
    channel = grpc.insecure_channel(CHANNEL_IP)
    stub = intent_slot_service_pb2_grpc.ISServiceStub(channel)
    message = 'do khoa khoa học và kỹ thuật máy tính tổ chức á'
    message = word_tokenize(message, format="text")
    result = stub.IntentSlotRecognize(intent_slot_service_pb2.IntentSlotRecognizeRequest(message=message))
    print(json.loads(result.message))
    
if __name__ == "__main__":
    main()