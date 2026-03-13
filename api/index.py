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
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Axedraxos AI</title>
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 50px;
                border: 1px solid #30363d;
                border-radius: 15px;
                background-color: #161b22;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5);
                max-width: 500px;
            }
            h1 {
                color: #58a6ff;
                margin-bottom: 10px;
            }
            p {
                font-size: 16px;
                line-height: 1.5;
                color: #8b949e;
                margin-bottom: 30px;
            }
            .status-badge {
                padding: 8px 16px;
                background-color: #238636;
                color: #ffffff;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
                display: inline-block;
                border: 1px solid #2ea043;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Axedraxos AI</h1>
            <p>Advanced data analytics and intelligent forecasting agent on the Base network.</p>
            <div class="status-badge">🟢 System Online & Healthy</div>
        </div>
    </body>
    </html>
    """
    return html_content

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
        "description": "Open Agent Semantic Framework endpoint for Axedraxos.",
        "skills": [
            {"name": "nlp/text_generation", "type": "cognitive"},
            {"name": "nlp/contextual_comprehension", "type": "cognitive"},
            {"name": "automation/workflow_automation", "type": "operational"},
            {"name": "nlp/conversational_ai", "type": "cognitive"}
        ],
        "domains": [
            "ai/machine_learning/deep_learning",
            "data_science/data_collection",
            "data_science/experimentation",
            "software_engineering/api_integration",
            "software_engineering/web_development"
        ],
        "protocols": ["mcp", "a2a"]
    })
