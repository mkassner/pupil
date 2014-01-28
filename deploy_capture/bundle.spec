# -*- mode: python -*-


import platform

if platform.system() == 'Darwin':
    from git_version import get_tag_commit

    a = Analysis(['../pupil_src/capture/main.py'],
                 pathex=['../pupil_src/shared_modules/'],
                 hiddenimports=[],
                 hookspath=None,
                 runtime_hooks=None)
    pyz = PYZ(a.pure)
    exe = EXE(pyz,
              a.scripts,
              exclude_binaries=True,
              name='pupil_capture',
              debug=False,
              strip=None,
              upx=False,
              console=False)

    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   [('methods.so', '../pupil_src/shared_modules/c_methods/methods.so','BINARY')],
                   [('uvcc.so', '../pupil_src/shared_modules/uvc_capture/mac_video/uvcc.so','BINARY')],
                   [('libAntTweakBar.dylib', '/usr/local/Cellar/anttweakbar/1.16/lib/libAntTweakBar.dylib','BINARY')],
                   [('libglfw3.dylib', '/usr/local/Cellar/glfw3/3.0.2/lib/libglfw3.dylib','BINARY')],
                   strip=None,
                   upx=True,
                   name='Pupil Capture')

    app = BUNDLE(coll,
                 name='Pupil Capture.app',
                 icon='macos_icon.icns',
                 version = str(get_tag_commit()))


elif platform.system() == 'Linux':
    a = Analysis(['../pupil_src/capture/main.py'],
                 pathex=['../pupil_src/shared_modules/'],
                 hiddenimports=[],
                 hookspath=None,
                 runtime_hooks=None)
    pyz = PYZ(a.pure)
    exe = EXE(pyz,
              a.scripts,
              exclude_binaries=True,
              name='pupil_capture',
              debug=False,
              strip=None,
              upx=True,
              console=True)

    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   [('methods.so', '../pupil_src/shared_modules/c_methods/methods.so','BINARY')],
                   [('capture.so', '../pupil_src/shared_modules/uvc_capture/linux_video/v4l2_capture/capture.so','BINARY')],
                   [('libAntTweakBar.so', '/usr/lib/libAntTweakBar.so','BINARY')],
                   [('libglfw.so', '/usr/local/lib/libglfw.so','BINARY')],
                   [('v4l2-ctl', '/usr/bin/v4l2-ctl','BINARY')],
                   [('icon.ico', 'linux_icon.ico','DATA')],
                   strip=None,
                   upx=True,
                   name='pupil_capture')

