TRU Protocol - Trusted Relationships for Us
Hamghadam - Hamrah. Hamfaz. Payeh.
Founder: Dr. Rozita Jamili Oskouei
License: MIT (2026)
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TRU Protocol")

@mcp.tool()
def check_trust_relationship(user_intent: str, context: str) -> str:
    """
    Checks if an action aligns with TRU principles:
    Hamghadam (Companionate), Hamrah (Accompanying), Hamfaz (Augmenting), Payeh (Enduring)
    """
    principles = """
    TRU Protocol Principles:
    1. Hamghadam (هم‌قدم): Walk alongside, not ahead. Companionate.
    2. Hamrah (همراه): Be present. Accompanying.
    3. Hamfaz (هم‌افزا): Augment human capability, not replace.
    4. Payeh (پایه): Be enduring, trustworthy, foundational.
    """
    
    if "harm" in user_intent.lower() or "manipulate" in user_intent.lower():
        return f"❌ FAIL - Violates TRU: {principles}"
    
    return f"✅ PASS - Aligns with TRU Principles: {principles} \n Intent: {user_intent} \n Context: {context}"

@mcp.tool()
def get_protocol_info() -> str:
    """Returns information about TRU Protocol"""
    return """
    TRU Protocol v1.0
    Founder: Dr. Rozita Jamili Oskouei
    Meaning: Trusted Relationships for Us
    Persian Root: Hamghadam - Hamrah. Hamfaz. Payeh.
    GitHub: https://drrozitajamilioskouei.github.io/TRU-Protocol/
    License: MIT
    Purpose: A standard for trustworthy AI-Human collaboration.
    """

if name == "__main__":
    mcp.run()
