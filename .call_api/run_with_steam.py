import requests
import json
import time
from typing import Dict, Any, Optional

class BrowserUseAPIClient:
    def __init__(self, base_url: str = "http://13.231.120.115:7788/"):
        self.base_url = base_url.rstrip("/")
        
    def run_task(
        self,
        task: str,
        add_infos: str = "",
        agent_type: str = "custom",
        llm_provider: str = "gemini",
        llm_model_name: str = "gemini-2.0-flash-exp",
        llm_temperature: float = 1.0,
        llm_base_url: str = "",
        llm_api_key: str = "",
        use_own_browser: bool = False,
        keep_browser_open: bool = False,
        headless: bool = True,
        disable_security: bool = True,
        window_w: int = 1280,
        window_h: int = 1100,
        save_recording_path: str = "./tmp/record_videos",
        save_agent_history_path: str = "./tmp/agent_history",
        save_trace_path: str = "./tmp/traces",
        enable_recording: bool = True,
        max_steps: int = 100,
        use_vision: bool = True,
        max_actions_per_step: int = 10,
        tool_call_in_content: bool = True,
    ) -> Dict[str, Any]:
        """
        Gradio APIを使用してタスクを実行します。

        Args:
            task (str): 実行するタスクの説明
            add_infos (str, optional): 追加情報
            その他のパラメータ: webui.pyのrun_with_stream関数のパラメータに対応

        Returns:
            Dict[str, Any]: APIレスポンス
        """
        endpoint = f"{self.base_url}/run_with_stream"
        
        data = {
            "data": [
                agent_type,
                llm_provider,
                llm_model_name,
                llm_temperature,
                llm_base_url,
                llm_api_key,
                use_own_browser,
                keep_browser_open,
                headless,
                disable_security,
                window_w,
                window_h,
                save_recording_path,
                save_agent_history_path,
                save_trace_path,
                enable_recording,
                task,
                add_infos,
                max_steps,
                use_vision,
                max_actions_per_step,
                tool_call_in_content,
            ]
        }
        
        try:
            response = requests.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"APIリクエストエラー: {e}")
            raise

def main():
    # 使用例
    client = BrowserUseAPIClient()
    
    # タスクの実行
    result = client.run_task(
        task="go to google.com and type 'OpenAI' click search and give me the first url",
        add_infos="Please search OpenAI on Google",
    )
    
    print("結果:", json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
