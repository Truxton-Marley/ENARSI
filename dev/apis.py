import common_prompts as cp

questions_apis = [
{
"question" : """
######################
###     APIs       ###
######################

SOAP:
    Envelope
    Header (opt)
    Body
    Fault (opt)

# SOAP Message:
<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope/" soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
    <soap:Header>
    </soap:Header>
    <soap:Body>
      <soap:Fault>
      </soap:Fault>
    </soap:Body>
</soap:Envelope>

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
XML-RPC

# Request:
    <methodCall>
    </methodCall>
# Response:
    <methodResonse>
    </methodResponse>

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Web hooks

Event-Driven

Client registers a URL with the server (Callback URL)
Server can then send HTTP POST requests to the client

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# API Sequence Diagram

UML - Unified Modeling Language

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Response Codes:

200 OK
201 Created
204 No Content

400 Bad Request
401 Unauthorized
403 Forbidden
405 Method not Allowed
408 Request Timeout
409 Conflict 

500 Internal Server Error
501 Method not Implemented
502 Bad Gateway
503 Services Unavailable
504 Gateway Timeout

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Rate Limit Algorithms
    Leaky Bucket (FIFO), Fix Window, Sliding Log, Sliding Window, Token Bucket

X-Ratelimit-Limit
X-Ratelimit-Remaining
X-Ratelimit-Reset

//---

/devices?offset=100&limit=15

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
gRPC
    Faster than JSON based APIs
    User Protocol Buffers (protobuf)
    Uses Proto files
    Relies on HTTP/2, but lacks current browser support

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Basic Auth:
    Base64 encoding of <username>:<password>
    Header:
        Authorization: "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=="

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]
