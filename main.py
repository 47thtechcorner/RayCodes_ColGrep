import os
import sys
import argparse
from pathlib import Path
import ollama

def run_agent_query(repo_path: str, query: str):
    """Executes code localization using the local colgrep-agent-2B model via Ollama."""
    system_prompt = (
        "You are ColGrep-Agent-2B, an expert code-localization specialist. "
        "Analyze queries about codebases and return exact file paths and line ranges in the format "
        "'path/to/file:START-END' along with a concise explanation."
    )
    
    user_prompt = f"Find code locations for query in {repo_path}: '{query}'"
    
    response = ollama.chat(
        model="colgrep-agent-2B",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    result_text = response["message"]["content"]
    
    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "outputs.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# ColGrep Agent Code Search Results\n\n")
        f.write(f"**Query:** {query}\n\n")
        f.write(f"**Target Scope:** `{repo_path}`\n\n")
        f.write("## Discovered Code Locations\n\n")
        f.write(f"{result_text}\n")
        
    return result_text

def main():
    parser = argparse.ArgumentParser(description="ColGrep Agent 2B Code Localization")
    parser.add_argument(
        "--query",
        type=str,
        default="where does the application handle task retry backoff and send failure notifications",
        help="Code search question"
    )
    parser.add_argument(
        "--repo",
        type=str,
        default="inputs/sample_app",
        help="Path to repository or code directory"
    )
    args = parser.parse_args()

    run_agent_query(args.repo, args.query)

if __name__ == "__main__":
    main()
