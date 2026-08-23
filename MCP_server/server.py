import os
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terraform-infrastructure-mcp")

# Terraform root directory
TERRAFORM_DIR = Path(
    os.getenv(
        "TERRAFORM_DIR",
        str(Path(__file__).resolve().parent.parent / "terraform")
    )
).resolve()


def run_terraform(command: list[str]) -> str:
    """
    Execute a Terraform command inside the Terraform directory.
    """

    result = subprocess.run(
        command,
        cwd=TERRAFORM_DIR,
        capture_output=True,
        text=True,
        timeout=600
    )

    output = result.stdout

    if result.stderr:
        output += "\n--- STDERR ---\n"
        output += result.stderr

    output += f"\n--- EXIT CODE: {result.returncode} ---"

    return output


@mcp.tool()
def terraform_validate() -> str:
    """
    Validate Terraform configuration.
    """

    return run_terraform(
        ["terraform", "validate"]
    )


@mcp.tool()
def terraform_fmt_check() -> str:
    """
    Check Terraform formatting.
    """

    return run_terraform(
        ["terraform", "fmt", "-check", "-recursive"]
    )


@mcp.tool()
def terraform_plan() -> str:
    """
    Run Terraform plan.
    Does not modify Azure infrastructure.
    """

    return run_terraform(
        [
            "terraform",
            "plan",
            "-input=false"
        ]
    )


@mcp.tool()
def terraform_apply() -> str:
    """
    Apply Terraform infrastructure.

    WARNING:
    This performs real infrastructure changes.
    """

    if os.getenv("ALLOW_TERRAFORM_APPLY", "false").lower() != "true":
        return (
            "Terraform apply is disabled. "
            "Set ALLOW_TERRAFORM_APPLY=true after approval."
        )

    return run_terraform(
        [
            "terraform",
            "apply",
            "-input=false",
            "-auto-approve"
        ]
    )


@mcp.tool()
def terraform_output() -> str:
    """
    Get Terraform outputs.
    """

    return run_terraform(
        [
            "terraform",
            "output"
        ]
    )


@mcp.tool()
def terraform_state_list() -> str:
    """
    List resources currently tracked in Terraform state.
    """

    return run_terraform(
        [
            "terraform",
            "state",
            "list"
        ]
    )


@mcp.tool()
def terraform_show() -> str:
    """
    Show current Terraform state.
    """

    return run_terraform(
        [
            "terraform",
            "show"
        ]
    )


@mcp.tool()
def azure_resource_check(resource_name: str) -> str:
    """
    Check whether an Azure resource exists using Azure CLI.
    """

    result = subprocess.run(
        [
            "az",
            "resource",
            "show",
            "--name",
            resource_name,
            "--output",
            "json"
        ],
        capture_output=True,
        text=True,
        timeout=120
    )

    if result.returncode != 0:
        return (
            f"Resource '{resource_name}' was not found "
            "or Azure CLI authentication failed.\n"
            + result.stderr
        )

    return result.stdout


@mcp.tool()
def terraform_status() -> str:
    """
    Return Terraform working directory and initialization status.
    """

    terraform_dir = str(TERRAFORM_DIR)

    if not TERRAFORM_DIR.exists():
        return f"Terraform directory does not exist: {terraform_dir}"

    return (
        f"Terraform directory: {terraform_dir}\n"
        f"Directory exists: True"
    )


if __name__ == "__main__":
    mcp.run()