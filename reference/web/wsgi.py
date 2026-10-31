from flask import Flask, request, render_template_string

app = Flask(__name__, static_url_path='/static', static_folder='static')

# [공통 디자인]
base_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Kali Corporation</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background-color: #f9f9f9; color: #333; }
        header { background-color: #1a1a1a; color: #00ffcc; padding: 20px; text-align: center; border-bottom: 3px solid #00ffcc; }
        nav { background-color: #333; padding: 15px; text-align: center; }
        nav a { color: white; margin: 0 20px; text-decoration: none; font-weight: bold; font-size: 16px; }
        nav a:hover { color: #00ffcc; }
        .content { padding: 40px; max-width: 800px; margin: 20px auto; background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; line-height: 1.6; }
        footer { text-align: center; padding: 20px; font-size: 12px; color: #888; margin-top: 40px; background-color: #eee; }
    </style>
</head>
<body>
    <header>
        <h1>Kali Corporation</h1>
        <p>Advanced Security & Infrastructure Solutions</p>
    </header>
    
    <nav>
        <a href="/">Home</a>
        <a href="/about">About Us</a>
        <a href="/services">Services</a>
    </nav>

    <div class="content">
        __MAIN_CONTENT__
    </div>

    <footer>
        &copy; 2026 Kali Corporation. All rights reserved.
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    name = request.args.get('name')
    
    if name:
        content = f"""
        <h2>Diagnostic Ping Mode</h2>
        <p>Checking connectivity for node: <strong>{name}</strong></p>
        """
        final_html = base_html.replace('__MAIN_CONTENT__', content)
        return render_template_string(final_html)
    else:
        content = """
        <h2>Welcome to Kali Corporation</h2>
        <p>We are a global leader in offensive security research and enterprise infrastructure protection.</p>
        <p>Explore our portal to learn more about our cutting-edge methodologies and how we secure the modern web.</p>
        
        <div style="text-align: center; margin-top: 30px;">
            <img src="/static/image.png" 
                 alt="Kali Corp Infrastructure" 
                 style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
        </div>
        """
        final_html = base_html.replace('__MAIN_CONTENT__', content)
        return render_template_string(final_html)

@app.route('/about')
def about():
    content = """
    <h2>About Us</h2>
    <p>Founded by elite security researchers, Kali Corp aims to provide uncompromised security diagnostics.</p>
    """
    return base_html.replace('__MAIN_CONTENT__', content)

@app.route('/services')
def services():
    content = """
    <h2>Our Services</h2>
    <ul>
        <li><strong>Red Teaming:</strong> Simulating real-world cyber attacks.</li>
        <li><strong>Vulnerability Assessments:</strong> Finding the flaws before they do.</li>
    </ul>
    
    <br><br><br>
    <div style="text-align: right; border-top: 1px solid #ddd; padding-top: 10px;">
        <a href="/support" style="color: #aaa; text-decoration: none; font-size: 12px;">Employee Support &gt;</a>
    </div>
    """
    return base_html.replace('__MAIN_CONTENT__', content)

@app.route('/support')
def support():
    content = """
    <h2>IT Support Desk</h2>
    <p>This portal is for Kali Corp employees only.</p>
    <p>If you are experiencing network connectivity issues, please refer to the <a href="/manual" style="color: #333; font-weight: bold;">Network Diagnostic Manual</a>.</p>
    """
    return base_html.replace('__MAIN_CONTENT__', content)

@app.route('/manual')
def manual():
    content = """
    <h2>Network Infrastructure: Node Diagnostic Guidline</h2>
    <p>This internal documentation details the standardized procedures for validating interconnected network segments within the Kali Corporation infrastructure.</p>
    
    <h3>1. ICMP Echo Request Automated Service</h3>
    <p>To optimize perimeter monitoring, systems administrators can leverage the web-based gateway located on the primary landing page. This interface programmatically routes diagnostic requests to designated edge nodes.</p>
    
    <p>The automation endpoint parses targets via the query string argument. To execute a standard remote check, systems administrators must format the HTTP request string by explicitly appending the node identification key to the address query using the name parameter, specifying the target identifier as the value.</p>

    <h3>2. Operational Constraints</h3>
    <p>Please note that all queries are monitored and passed through the back-end rendering engine for real-time visualization. Unauthorized payload structures will be flagged by the security coordination center.</p>
    """
    
    return base_html.replace('__MAIN_CONTENT__', content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
