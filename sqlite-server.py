# sqlite-server.py
from mcp.server.fastmcp import FastMCP
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "community.db")

# Initialize the MCP server with a friendly name
mcp = FastMCP("Community Chatters")

# Define a tool to fetch the top chatters from the SQLite database
@mcp.tool()
def get_top_chatters():
    """Retrieve the top chatters sorted by number of messages."""
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Execute the query to fetch chatters sorted by messages
    cursor.execute("SELECT name, messages FROM chatters ORDER BY messages DESC")
    results = cursor.fetchall()
    conn.close()
    
    # Format the results as a list of dictionaries
    chatters = [{"name": name, "messages": messages} for name, messages in results]
    return chatters

# Run the MCP server locally
if __name__ == '__main__':
    mcp.run()
