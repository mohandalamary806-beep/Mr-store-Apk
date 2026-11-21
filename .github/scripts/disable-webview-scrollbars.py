from pathlib import Path
root = Path('android/app/src/main')
files = list(root.rglob('MainActivity.java')) + list(root.rglob('MainActivity.kt'))
if not files:
    raise SystemExit('MainActivity not found; cannot disable native WebView scrollbars')
p = files[0]
s = p.read_text()
if p.suffix == '.java':
    if 'setVerticalScrollBarEnabled(false)' not in s:
        s=s.replace('import com.getcapacitor.BridgeActivity;', 'import com.getcapacitor.BridgeActivity;\nimport android.os.Bundle;')
        s=s.replace('public class MainActivity extends BridgeActivity {', '''public class MainActivity extends BridgeActivity {\n    @Override\n    public void onCreate(Bundle savedInstanceState) {\n        super.onCreate(savedInstanceState);\n        getBridge().getWebView().setVerticalScrollBarEnabled(false);\n        getBridge().getWebView().setHorizontalScrollBarEnabled(false);\n    }''')
else:
    if 'isVerticalScrollBarEnabled = false' not in s:
        s=s.replace('import com.getcapacitor.BridgeActivity', 'import com.getcapacitor.BridgeActivity\nimport android.os.Bundle')
        s=s.replace('class MainActivity : BridgeActivity()', '''class MainActivity : BridgeActivity() {\n    override fun onCreate(savedInstanceState: Bundle?) {\n        super.onCreate(savedInstanceState)\n        bridge?.webView?.isVerticalScrollBarEnabled = false\n        bridge?.webView?.isHorizontalScrollBarEnabled = false\n    }\n}''')
p.write_text(s)
print(f'Patched native WebView scrollbars: {p}')
