class FTCommandsBuilder:

    def __init__(self, network_id: str, node_url: str) -> None:
        self.network_id = network_id
        self.node_url = node_url

    def get_token_metadata(self, token: str) -> str:
        json_args = "{}"
        return f"near --quiet contract call-function as-read-only {token} ft_metadata json-args {json_args} network-config {self.network_id} now"