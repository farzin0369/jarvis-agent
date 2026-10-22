# Jarvis Agent (Free)

دستیار هوشمند شخصی رایگان که روی GitHub Actions اجرا می‌شود.

## راه‌اندازی

1. برو به [OpenRouter](https://openrouter.ai) و یک API Key رایگان بگیر.
2. در این ریپو: Settings → Secrets and variables → Actions → New repository secret
   - Name: `OPENROUTER_API_KEY`
   - Value: کلیدت
3. برو به تب Actions و workflow را اجرا کن.

## اجرای دستی

در تب Actions → Jarvis Agent → Run workflow


## رابط چت وب

فایل `chat.html` یک رابط چت فارسی است که پیام‌ها را با `workflow_dispatch` به همین مخزن می‌فرستد و پاسخ هر اجرا را از Check Summary می‌خواند. تاریخچهٔ گفتگو در مرورگر نگه‌داری می‌شود؛ هر پیام تازه همراه با بخش اخیر تاریخچه به workflow می‌رود.

### فعال‌سازی

1. در **Settings → Pages**، بخش **Build and deployment** را روی **Deploy from a branch** بگذار، شاخهٔ `main` و پوشهٔ `/(root)` را انتخاب کن و ذخیره کن.
2. پس از انتشار Pages، صفحهٔ گفتگو در `https://farzin0369.github.io/jarvis-agent/chat.html` در دسترس است.
3. مطمئن شو در **Settings → Secrets and variables → Actions**، secret به نام `OPENROUTER_API_KEY` تنظیم شده است.
4. در صفحهٔ چت، از دکمهٔ تنظیمات یک **Fine-grained personal access token** بساز که فقط به این مخزن دسترسی داشته باشد و مجوزهای **Actions: Read and write** و **Checks: Read-only** را داشته باشد. توکن در `localStorage` همین مرورگر ذخیره می‌شود و با پاک‌کردن داده‌های سایت یا دکمهٔ حذف توکن قابل حذف است.

هر پیام یک اجرای GitHub Actions ایجاد می‌کند؛ بنابراین پاسخ به زمان اجرای Actions و محدودیت‌های GitHub و مدل‌های رایگان OpenRouter وابسته است. مخزن عمومی است؛ خروجی اجرا را خصوصی فرض نکن و اطلاعات حساس را داخل پیام‌ها نفرست.
