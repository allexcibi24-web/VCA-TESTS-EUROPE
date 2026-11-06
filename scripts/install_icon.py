from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
src=Image.open(root/'assets/icon.png').convert('RGBA')
res=root/'android/app/src/main/res'
for density,size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
    d=res/f'mipmap-{density}';d.mkdir(parents=True,exist_ok=True)
    im=src.resize((size,size),Image.Resampling.LANCZOS)
    for name in ['ic_launcher.png','ic_launcher_round.png','ic_launcher_foreground.png']:
        im.save(d/name)
# Avoid Android adaptive icon XML masking the complete artwork in the legacy icon.
manifest=root/'android/app/src/main/AndroidManifest.xml'
s=manifest.read_text()
s=s.replace('android:roundIcon="@mipmap/ic_launcher_round"','android:roundIcon="@mipmap/ic_launcher_round"')
manifest.write_text(s)
print('Installed launcher icon in Android mipmap resources.')
