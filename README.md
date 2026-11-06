# VCA Tests Europe — V1.0 (Android starter)

Prima versiune destinată instalării ca aplicație Android. Antetul afișează **PREMIUM • V1.0**.

## Conținut
- 5 limbi: română, engleză, franceză, germană, olandeză
- Lecții VCA, Manual Handling, Abrasive Wheels, examene și certificate de absolvire online
- Light/Dark Mode și solicitarea numelui la fiecare deschidere
- `www/index.html` este pagina folosită de Capacitor în APK
- `index.html` este o copie pentru testarea directă în browser

## APK de test prin GitHub Actions
1. Creează un repository GitHub nou (sau folosește un branch separat).
2. Încarcă **conținutul** acestui folder, păstrând inclusiv `.github/workflows/android-apk.yml`.
3. Intră la Actions → VCA Tests Europe - Android APK → Run workflow (sau împinge modificările pe `main`).
4. După build, descarcă artifactul `VCA-Tests-Europe-debug-APK`, dezarhivează și instalează `app-debug.apk`.

Acesta este un proiect-sursă, **nu** un APK compilat. Build-ul Android nu a fost verificat local. Pentru publicare pe Google Play este necesar un build de release semnat (de regulă AAB).

**Notă:** conținutul de instruire și traducerile necesită revizuire de specialitate și testare completă înainte de distribuirea comercială. Certificatele nu sunt acreditate.
