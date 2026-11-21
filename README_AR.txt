MR Store - ملفات إصلاح GitHub Actions و Google Sign-In

محتويات الحزمة:
1) package.json
   - تثبيت إضافة Google Auth على الإصدار المنشور لـ Capacitor 6: 3.4.0-rc.4
2) capacitor.config.json
   - إضافة Android OAuth Client ID الجديد.
   - الإبقاء على Web Client ID الحالي داخل serverClientId.
3) .github/workflows/android-apk.yml
   - إنشاء Debug keystore عند غيابه.
   - تخزينه مؤقتًا في GitHub Actions Cache للمحافظة على SHA-1 بين عمليات البناء المتكررة.
   - طباعة SHA-1 وSHA-256 من ملف APK النهائي نفسه.

طريقة التركيب:
- استبدل package.json الموجود في جذر المستودع.
- استبدل capacitor.config.json الموجود في جذر المستودع.
- استبدل .github/workflows/android-apk.yml مع الحفاظ على المسار.
- اعمل Commit للتغييرات على main.
- افتح Actions وتابع Build MR Store APK.
- بعد نجاح البناء، افتح خطوة Print SHA-1 from the built APK؛ هذه هي بصمة ملف APK المرفوع في نفس العملية.

تنبيهات:
- هذه الحزمة لا تحتوي على APK مبني؛ GitHub Actions سيبنيه بعد رفع الملفات.
- Cache مناسب للاختبار المستمر لكنه ليس بديلًا عن إدارة مفتاح توقيع Release بشكل خاص ودائم عند النشر.
- لا ترفع ملف keystore أو كلمات مروره داخل مستودع عام.
