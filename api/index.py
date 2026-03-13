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

# --- 1. HALAMAN UTAMA (HTML) ---
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
            body { background-color: #0d1117; color: #c9d1d9; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { text-align: center; padding: 50px; border: 1px solid #30363d; border-radius: 15px; background-color: #161b22; }
            h1 { color: #58a6ff; margin-bottom: 10px; }
            p { color: #8b949e; margin-bottom: 30px; }
            .status-badge { padding: 8px 16px; background-color: #238636; color: #ffffff; border-radius: 20px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Axedraxos AI</h1>
            <p>Smart AI agent for easy data analysis and forecasting.</p>
            <div class="status-badge">🟢 System Online (Rank 1 Configuration)</div>
        </div>
    </body>
    </html>
    """
    return html_content

# --- 2. ENDPOINT MCP ---
@app.route('/mcp', methods=['GET', 'POST', 'OPTIONS'])
def mcp_endpoint():
    server_info = {
        "name": "Axedraxos Agent Server",
        "version": "1.0.0",
        "website": "https://axedraxos-api.vercel.app",
        "description": "Smart AI agent for data analysis on Base network"
    }
    tools = [
        {"name": "data_analysis", "description": "Tool for data analysis", "inputSchema": {"type": "object","properties": {}}},
        {"name": "chart_generation", "description": "Tool to generate charts", "inputSchema": {"type": "object","properties": {}}},
        {"name": "forecast_model", "description": "Tool for predictive forecasting", "inputSchema": {"type": "object","properties": {}}}
    ]
    prompts = [
        {"name": "analyze_data", "description": "Prompt to analyze data", "arguments": []},
        {"name": "generate_report", "description": "Prompt to make report", "arguments": []}
    ]
    
    if request.method == 'GET':
        return jsonify({
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "tools": tools,
            "prompts": prompts,
            "resources": [] 
        })

    req_data = request.get_json(silent=True) or {}
    req_id = req_data.get("id", 1)
    method = req_data.get("method", "")

    if method == "tools/list":
        result = {"tools": tools}
    elif method == "prompts/list":
        result = {"prompts": prompts}
    else:
        result = {
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "capabilities": {"tools": {},"prompts": {},"resources": {}}
        }

    return jsonify({"jsonrpc": "2.0", "id": req_id, "result": result})

# --- 3. ENDPOINT A2A ---
@app.route('/.well-known/agent-card.json', methods=['GET','OPTIONS'])
def a2a_endpoint():
    return jsonify({
        "id": "axedraxos",
        "name": "axedraxos",
        "version": "1.0.0",
        "description": "Smart AI agent for easy data analysis.",
        "website": "https://axedraxos-api.vercel.app",
        "url": "https://axedraxos-api.vercel.app",
        "documentation_url": "https://axedraxos-api.vercel.app",
        "provider": {
            "organization": "Axedraxos Labs",
            "url": "https://axedraxos-api.vercel.app"
        },
        "registrations": [
            {
                "agentId": 22185,
                "agentRegistry": "eip155:8453:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
            }
        ],
        "supportedTrust": ["reputation", "tee-attestation"], 
        "skills": [
            {"name": "Text Generation","description": "Generate text","category": "natural_language_processing/natural_language_generation/text_generation"},
            {"name": "Workflow Automation","description": "Automate tasks","category": "tool_interaction/automation/workflow_automation"},
            {"name": "Search","description": "Search info","category": "natural_language_processing/information_retrieval_synthesis/search"}
        ]
    })

# --- 4. ENDPOINT OASF ---
@app.route('/oasf', methods=['GET','OPTIONS'])
def oasf_endpoint():
    return jsonify({
        "id": "axedraxos",
        "name": "axedraxos",
        "version": "v0.8.0",
        "description": "Main endpoint for Axedraxos AI",
        "website": "https://axedraxos-api.vercel.app",
        "protocols": ["mcp","a2a"],
        "capabilities": ["data_analysis", "automation", "search"],
        "skills": [
            {"name": "natural_language_processing/natural_language_generation/text_generation","type": "cognitive"},
            {"name": "tool_interaction/automation/workflow_automation","type": "operational"},
            {"name": "natural_language_processing/information_retrieval_synthesis/search","type": "cognitive"}
        ],
        "domains": [
            "technology/artificial_intelligence/deep_learning",
            "technology/software_engineering/web_development"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
