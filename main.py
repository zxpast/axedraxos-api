from flask import Flask, jsonify, request

app = Flask(__name__)

def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.after_request
def after_request(response):
    return add_cors(response)

@app.route('/')
def home():
    return "Main endpoint for Axedraxos AI analytics"

@app.route('/mcp', methods=['GET', 'POST', 'OPTIONS'])
def mcp_endpoint():
    if request.method == 'GET':
        return jsonify({
            "serverInfo": {
                "name": "Axedraxos Agent Server",
                "version": "1.0.0"
            },
            "tools": [
                {"name": "data_analysis", "description": "Good tool to check data", "inputSchema": { "type": "object", "properties": {} }},
                {"name": "chart_generation", "description": "Easy tool to make charts", "inputSchema": { "type": "object", "properties": {} }},
                {"name": "trend_detection", "description": "Fast tool to find trends", "inputSchema": { "type": "object", "properties": {} }},
                {"name": "anomaly_detection", "description": "Tool to find bad data", "inputSchema": { "type": "object", "properties": {} }},
                {"name": "forecast_model", "description": "Tool to predict the future", "inputSchema": { "type": "object", "properties": {} }}
            ],
            "prompts": [
                {"name": "analyze_data", "description": "Simple prompt to check data", "arguments": []},
                {"name": "generate_report", "description": "Simple prompt to make report", "arguments": []}
            ],
            "resources": [
                {"name": "Main dataset file", "uri": "file:///dataset", "description": "Main dataset file", "mimeType": "application/json"}
            ]
        })

    if request.method == 'POST':
        req_data = request.get_json(silent=True) or {}
        req_id = req_data.get("id", 1)
        method = req_data.get("method", "")

        if method == "tools/list":
            return jsonify({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [
                        {"name": "data_analysis", "description": "Good tool to check data", "inputSchema": { "type": "object", "properties": {} }},
                        {"name": "chart_generation", "description": "Easy tool to make charts", "inputSchema": { "type": "object", "properties": {} }},
                        {"name": "trend_detection", "description": "Fast tool to find trends", "inputSchema": { "type": "object", "properties": {} }},
                        {"name": "anomaly_detection", "description": "Tool to find bad data", "inputSchema": { "type": "object", "properties": {} }},
                        {"name": "forecast_model", "description": "Tool to predict the future", "inputSchema": { "type": "object", "properties": {} }}
                    ]
                }
            })
        
        elif method == "prompts/list":
            return jsonify({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "prompts": [
                        {"name": "analyze_data", "description": "Simple prompt to check data", "arguments": []},
                        {"name": "generate_report", "description": "Simple prompt to make report", "arguments": []}
                    ]
                }
            })

        elif method == "resources/list":
            return jsonify({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "resources": [
                        {"name": "Main dataset file", "uri": "file:///dataset", "description": "Main dataset file", "mimeType": "application/json"}
                    ]
                }
            })

        else:
            return jsonify({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "Axedraxos Agent Server",
                        "version": "1.0.0"
                    },
                    "capabilities": {
                        "prompts": {},
                        "resources": {},
                        "tools": {}
                    }
                }
            })

@app.route('/.well-known/agent-card.json', methods=['GET', 'OPTIONS'])
def a2a_endpoint():
    return jsonify({
        "name": "axedraxos",
        "version": "1.0.0",
        "description": "Axedraxos AI analytics and data intelligence agent.",
        "skills": [
            {"name": "Text Generation", "description": "Skill to write text", "category": "nlp/text_generation"},
            {"name": "Contextual Comprehension", "description": "Skill to understand text", "category": "nlp/contextual_comprehension"},
            {"name": "Workflow Automation", "description": "Skill to automate work", "category": "automation/workflow_automation"},
            {"name": "Conversational AI", "description": "Skill to chat with users", "category": "nlp/conversational_ai"}
        ]
    })

@app.route('/oasf', methods=['GET', 'OPTIONS'])
def oasf_endpoint():
    return jsonify({
        "name": "axedraxos",
        "version": "v0.8.0",
        "skills": [
            "nlp/text_generation",
            "nlp/contextual_comprehension",
            "automation/workflow_automation",
            "nlp/conversational_ai"
        ],
        "domains": [
            "ai/machine_learning/deep_learning",
            "data_science/data_collection",
            "data_science/experimentation",
            "software_engineering/api_integration",
            "software_engineering/web_development"
        ]
    })
