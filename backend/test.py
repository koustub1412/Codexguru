from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="Salesforce/codegen-350M-multi",
    local_dir="models/codegen-350M-multi",
    local_dir_use_symlinks=False
)
