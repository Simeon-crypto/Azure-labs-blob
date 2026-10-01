# Azure Blob-Triggered Function

A Python Azure Function that automatically runs whenever a file is uploaded to
a Blob Storage container, and writes a summary file to a second container.

## Azure services used

- Azure Functions (Consumption plan)
- Azure Blob Storage (trigger + output binding)
- Event Grid (used behind the scenes for low-latency blob delivery)
- Application Insights (monitoring)

## What I learned

- How a blob trigger and output binding work together with no manual glue code
- The difference between polling-based and Event Grid-based blob triggers,
  and why newer Function Apps default to Event Grid
- How to test locally with Azurite before deploying anything real to Azure
- How to troubleshoot Git, Python environment, and Azure CLI/portal issues
  that come up when setting up a new machine for Azure development

## How to run it locally

```bash
git clone https://github.com/yourusername/repo-name.git
cd repo-name
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Start Azurite (via the VS Code Azurite extension, or `azurite` CLI), then:

```bash
func start
```

Upload a file into a local `incoming` container (via Azure Storage Explorer,
the VS Code Azure Storage extension, or the Azure CLI) to trigger it.

## Deploying to Azure

Deployed via the Azure Functions extension in VS Code
("Deploy to Azure" from the project folder). The Function App uses a
Consumption plan and reads/writes to its own storage account's `incoming`
and `processed` containers.

## Notes

- `local.settings.json` is excluded from this repo since it can contain
  local connection strings.
- The deployed version requires an Event Grid subscription wired to the
  `blob_trigger` function in order to receive blob-created events.
