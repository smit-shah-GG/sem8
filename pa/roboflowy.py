from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="http://localhost:9001",  # use local inference server
    api_key="5NJhlQs43M84eD36fKaj",
)

# result = client.run_workflow(
#     workspace_name="base-vjeus",
#     workflow_id="detect-count-and-visualize-2",
#     images={"image": "./PA dataset/coin_2.jpeg"},
# )
