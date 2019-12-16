%define _disable_ld_no_undefined 1

%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define py2verflags -python2.7
%define api %(echo %{version} |cut -d. -f1-2)

%define debug_package %{nil}

%bcond_without python2

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt5
Name:		pyside2
Version:	5.13.2
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
Source0:	https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-opensource-src-%{version}.tar.xz
Patch0:         python38_classifier.patch
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	python-numpy-devel
BuildRequires:	clang-devel
BuildRequires:	llvm-devel
BuildRequires:	pkgconfig(Qt5Bluetooth)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5Enginio)
BuildRequires:	pkgconfig(Qt5Nfc)
BuildRequires:	pkgconfig(Qt5PositioningQuick)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5Help)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5MultimediaWidgets)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5Positioning)
BuildRequires:	cmake(Qt5Location)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5RemoteObjects)
BuildRequires:	cmake(Qt5Scxml)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Sensors)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Charts)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5DataVisualization)
BuildRequires:	cmake(Qt5UiTools)
BuildRequires:	cmake(Qt5WebChannel)
BuildRequires:	cmake(Qt5WebEngineCore)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(Qt53DCore)
BuildRequires:	cmake(Qt53DRender)
BuildRequires:	cmake(Qt53DInput)
BuildRequires:	cmake(Qt53DLogic)
BuildRequires:	cmake(Qt53DAnimation)
BuildRequires:	cmake(Qt53DExtras)

# work around package bug
BuildRequires:	%{_lib}qt5positioningquick5
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5ScriptTools)
BuildRequires:	pkgconfig(Qt5Sensors)
BuildRequires:	pkgconfig(Qt5SerialPort)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	pkgconfig(Qt5WebChannel)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineCore)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5WebSockets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	qt5-qtqml-private-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
BuildRequires:	qt5-assistant
Requires:	pyside2-core
Requires:	pyside2-gui
Requires:	pyside2-help
Requires:	pyside2-multimedia
Requires:	pyside2-network
Requires:	pyside2-opengl
Requires:	pyside2-script
Requires:	pyside2-scripttools
Requires:	pyside2-sql
Requires:	pyside2-test
Requires:	pyside2-xmlpatterns
Requires:	pyside2-xml
Requires:	pyside2-uitools
Requires:	pyside2-svg
Requires:	pyside2-webengine
Requires:	pyside2-charts
Requires:	pyside2-concurrent
Requires:	pyside2-location
Requires:	pyside2-multimediawidgets
Requires:	pyside2-positioning
Requires:	pyside2-printsupport
Requires:	pyside2-qml
Requires:	pyside2-quick
Requires:	pyside2-quickwidgets
Requires:	pyside2-sensors
Requires:	pyside2-texttospeech
Requires:	pyside2-webchannel
Requires:	pyside2-websockets
Requires:	pyside2-widgets
Requires:	pyside2-x11extras
%if %{with python2}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:	python2-numpy-devel
%endif

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files

#------------------------------------------------------------------------------
%package -n shiboken2
Summary:	Python binding generator for Qt libraries
Group:		Development/KDE and Qt
Obsoletes:	shiboken2 < 5.13.0-2

%description -n shiboken2
Python binding generator for Qt libraries.

%files -n shiboken2
%{_bindir}/shiboken2
%{_bindir}/shiboken_tool.py
%{py_platsitedir}/shiboken2
%{py_platsitedir}/shiboken2_generator
%{_mandir}/man1/*
%{py_platsitedir}/shiboken2-%{version}-py3.7.egg-info
%{py_platsitedir}/shiboken2_generator-%{version}-py3.7.egg-info

#------------------------------------------------------------------------------
%define shibokenlib %mklibname shiboken2 %{api}
%package -n %{shibokenlib}
Summary:	Shiboken Generator core library
Group:		System/Libraries

%description -n %{shibokenlib}
Shiboken Generator core library.

%files -n %{shibokenlib}
%{_libdir}/libshiboken2*cpython*.so.%{api}*

#------------------------------------------------------------------------------
%if %{with python2}
%define shibokenlib_py2 %mklibname shiboken2_python2.7 %{api}

%package -n %{shibokenlib_py2}
Summary:	Shiboken Generator core library
Group:		System/Libraries

%description -n %{shibokenlib_py2}
Shiboken Generator core library.

%if %{with python2}
%files -n %{shibokenlib_py2}
%{_libdir}/libshiboken2*python2*.so.%{api}*
%endif

#------------------------------------------------------------------------------
%package -n python2-shiboken2
Summary:	PySide shiboken2 module for Python 2.x
Group:		Development/KDE and Qt

%description -n python2-shiboken2
PySide shiboken2 module for Python 2.x/.

%files -n python2-shiboken2
%{py2_platsitedir}/shiboken2
%{py2_platsitedir}/shiboken2_generator
%endif
#------------------------------------------------------------------------------

%package core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description core
PySide core module.

%files core
%{py_platsitedir}/PySide2/QtCore.*.so
%{py_platsitedir}/PySide2/__init__.py*
%{py_platsitedir}/PySide2/_config.py*
%{py_platsitedir}/PySide2/_git_pyside_version.py*
%{py_platsitedir}/PySide2/__pycache__
%{_libdir}/libpyside2.%{py3verflags}.so.%{api}*
%dir %{_datadir}/PySide2/glue
%{_datadir}/PySide2/glue/qtcore.cpp
%dir %{_datadir}/PySide2/typesystems
%{_datadir}/PySide2/typesystems/typesystem_core.xml
%{_datadir}/PySide2/typesystems/typesystem_core_x11.xml
%{_datadir}/PySide2/typesystems/*_common.xml
%{py_platsitedir}/PySide2-%{version}-py3.7.egg-info

#------------------------------------------------------------------------------

%package gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description gui
PySide gui module.

%files gui
%{py_platsitedir}/PySide2/QtGui.*.so
%{_datadir}/PySide2/typesystems/typesystem_gui*
%{_datadir}/PySide2/glue/qtgui.cpp

#------------------------------------------------------------------------------

%package 3d
Summary:	PySide 3D module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description 3d
PySide 3D module.

%files 3d
%{py_platsitedir}/PySide2/Qt3DAnimation.*.so
%{py_platsitedir}/PySide2/Qt3DCore.*.so
%{py_platsitedir}/PySide2/Qt3DExtras.*.so
%{py_platsitedir}/PySide2/Qt3DInput.*.so
%{py_platsitedir}/PySide2/Qt3DLogic.*.so
%{py_platsitedir}/PySide2/Qt3DRender.*.so
%{_datadir}/PySide2/typesystems/typesystem_3danimation.xml
%{_datadir}/PySide2/typesystems/typesystem_3dcore.xml
%{_datadir}/PySide2/typesystems/typesystem_3dextras.xml
%{_datadir}/PySide2/typesystems/typesystem_3dinput.xml
%{_datadir}/PySide2/typesystems/typesystem_3dlogic.xml
%{_datadir}/PySide2/typesystems/typesystem_3drender.xml

#------------------------------------------------------------------------------

%package help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description help
PySide help module.

%files help
%{py_platsitedir}/PySide2/QtHelp.*.so
%{_datadir}/PySide2/typesystems/typesystem_help.*

#------------------------------------------------------------------------------

%package multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description multimedia
PySide multimedia module.

%files multimedia
%{py_platsitedir}/PySide2/QtMultimedia.*.so
%{_datadir}/PySide2/typesystems/typesystem_multimedia.xml
%{_datadir}/PySide2/typesystems/typesystem_multimedia_*
%{_datadir}/PySide2/glue/qtmultimedia.cpp

#------------------------------------------------------------------------------

%package network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description network
PySide network module.

%files network
%{py_platsitedir}/PySide2/QtNetwork.*.so
%{_datadir}/PySide2/typesystems/typesystem_network.*
%{_datadir}/PySide2/glue/qtnetwork.cpp

#------------------------------------------------------------------------------

%package datavisualization
Summary:	PySide data visualization module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description datavisualization
PySide data visualization module.

%files datavisualization
%{py_platsitedir}/PySide2/QtDataVisualization.*.so
%{_datadir}/PySide2/typesystems/typesystem_datavisualization.*
%{_datadir}/PySide2/glue/qtdatavisualization.cpp


#------------------------------------------------------------------------------

%package remoteobjects
Summary:	PySide remote objects module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description remoteobjects
PySide remote objects module.

%files remoteobjects
%{py_platsitedir}/PySide2/QtRemoteObjects.*.so
%{_datadir}/PySide2/typesystems/typesystem_remoteobjects.*


#------------------------------------------------------------------------------

%package scxml
Summary:	PySide XML Scene Graph module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description scxml
PySide XML Scene Graph module.

%files scxml
%{py_platsitedir}/PySide2/QtScxml.*.so
%{_datadir}/PySide2/typesystems/typesystem_scxml.*


#------------------------------------------------------------------------------

%package opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description opengl
PySide opengl module.

%files opengl
%{py_platsitedir}/PySide2/QtOpenGL.*.so
%{py_platsitedir}/PySide2/QtOpenGLFunctions.*.so
%{_datadir}/PySide2/typesystems/typesystem_opengl*
%{_datadir}/PySide2/glue/qtopengl.cpp

#------------------------------------------------------------------------------

%package script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description script
PySide script module.

%files script
%{py_platsitedir}/PySide2/QtScript.*.so
%{_datadir}/PySide2/typesystems/typesystem_script.*
%{_datadir}/PySide2/glue/qtscript.cpp

#------------------------------------------------------------------------------

%package scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description scripttools
PySide scripttool module.

%files scripttools
%{py_platsitedir}/PySide2/QtScriptTools.*.so
%{_datadir}/PySide2/typesystems/typesystem_scripttools.*

#------------------------------------------------------------------------------

%package sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description sql
PySide sql module.

%files sql
%{py_platsitedir}/PySide2/QtSql.*.so
%{_datadir}/PySide2/typesystems/typesystem_sql.*

#------------------------------------------------------------------------------

%package svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description svg
PySide svg module.

%files svg
%{py_platsitedir}/PySide2/QtSvg.*.so
%{_datadir}/PySide2/typesystems/typesystem_svg.*

#------------------------------------------------------------------------------

%package test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description test
PySide test module.

%files test
%{py_platsitedir}/PySide2/QtTest.*.so
%{_datadir}/PySide2/typesystems/typesystem_test.*

#------------------------------------------------------------------------------

%package uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description uitools
PySide uitools module.

%files uitools
%{py_platsitedir}/PySide2/QtUiTools.*.so
%{_datadir}/PySide2/typesystems/typesystem_uitools.*
%{_datadir}/PySide2/glue/qtuitools.cpp

#------------------------------------------------------------------------------

%package webengine
Summary:	PySide webengine module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description webengine
PySide webengine module.

%files webengine
%{py_platsitedir}/PySide2/QtWebEngine*.so
%{_datadir}/PySide2/typesystems/typesystem_webengine*

#------------------------------------------------------------------------------

%package xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description xmlpatterns
PySide xmlpatterns module.

%files xmlpatterns
%{py_platsitedir}/PySide2/QtXmlPatterns.*.so
%{_datadir}/PySide2/typesystems/typesystem_xmlpatterns*
%{_datadir}/PySide2/glue/qtxmlpatterns.cpp

#------------------------------------------------------------------------------

%package xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description xml
PySide xml module.

%files xml
%{py_platsitedir}/PySide2/QtXml.*.so
%{_datadir}/PySide2/typesystems/typesystem_xml.*
%{_datadir}/PySide2/glue/qtxml.cpp

#------------------------------------------------------------------------------

%package charts
Summary:        PySide charts module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description charts
PySide charts module.

%files charts
%{py_platsitedir}/PySide2/QtCharts.*.so
%{_datadir}/PySide2/typesystems/typesystem_charts*

#------------------------------------------------------------------------------

%package concurrent
Summary:        PySide concurrent module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description concurrent
PySide concurrent module.

%files concurrent
%{py_platsitedir}/PySide2/QtConcurrent.*.so
%{_datadir}/PySide2/typesystems/typesystem_concurrent*

#------------------------------------------------------------------------------

%package location
Summary:        PySide location module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description location
PySide location module.

%files location
%{py_platsitedir}/PySide2/QtLocation.*.so
%{_datadir}/PySide2/typesystems/typesystem_location*

#------------------------------------------------------------------------------

%package multimediawidgets
Summary:        PySide multimediawidgets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description multimediawidgets
PySide multimediawidgets module.

%files multimediawidgets
%{py_platsitedir}/PySide2/QtMultimediaWidgets.*.so
%{_datadir}/PySide2/typesystems/typesystem_multimediawidgets*

#------------------------------------------------------------------------------

%package positioning
Summary:        PySide positioning module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description positioning
PySide positioning module.

%files positioning
%{py_platsitedir}/PySide2/QtPositioning.*.so
%{_datadir}/PySide2/typesystems/typesystem_positioning*

#------------------------------------------------------------------------------

%package printsupport
Summary:        PySide printsupport module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description printsupport
PySide printsupport module.

%files printsupport
%{py_platsitedir}/PySide2/QtPrintSupport.*.so
%{_datadir}/PySide2/typesystems/typesystem_printsupport*
%{_datadir}/PySide2/glue/qtprintsupport.cpp

#------------------------------------------------------------------------------

%package qml
Summary:        PySide qml module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description qml
PySide qml module.

%files qml
%{py_platsitedir}/PySide2/QtQml.*.so
%{_datadir}/PySide2/typesystems/typesystem_qml*
%{_datadir}/PySide2/glue/qtqml.cpp

#------------------------------------------------------------------------------

%package quick
Summary:        PySide quick module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description quick
PySide quick module.

%files quick
%{py_platsitedir}/PySide2/QtQuick.*.so
%{_datadir}/PySide2/typesystems/typesystem_quick.xml
%{_datadir}/PySide2/glue/qtquick.cpp

#------------------------------------------------------------------------------

%package quickwidgets
Summary:        PySide quickwidgets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description quickwidgets
PySide quickwidgets module.

%files quickwidgets
%{py_platsitedir}/PySide2/QtQuickWidgets.*.so
%{_datadir}/PySide2/typesystems/typesystem_quickwidgets*

#------------------------------------------------------------------------------

%package sensors
Summary:        PySide sensors module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description sensors
PySide sensors module.

%files sensors
%{py_platsitedir}/PySide2/QtSensors.*.so
%{_datadir}/PySide2/typesystems/typesystem_sensors*

#------------------------------------------------------------------------------

%package texttospeech
Summary:        PySide texttospeech module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description texttospeech
PySide texttospeech module.

%files texttospeech
%{py_platsitedir}/PySide2/QtTextToSpeech.*.so
%{_datadir}/PySide2/typesystems/typesystem_texttospeech*

#------------------------------------------------------------------------------

%package webchannel
Summary:        PySide webchannel module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description webchannel
PySide webchannel module.

%files webchannel
%{py_platsitedir}/PySide2/QtWebChannel.*.so
%{_datadir}/PySide2/typesystems/typesystem_webchannel*

#------------------------------------------------------------------------------

%package websockets
Summary:        PySide websockets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description websockets
PySide websockets module.

%files websockets
%{py_platsitedir}/PySide2/QtWebSockets.*.so
%{_datadir}/PySide2/typesystems/typesystem_websockets*

#------------------------------------------------------------------------------

%package widgets
Summary:        PySide widgets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description widgets
PySide widgets module.

%files widgets
%{py_platsitedir}/PySide2/QtWidgets.*.so
%{_datadir}/PySide2/typesystems/typesystem_widgets*
%{_datadir}/PySide2/glue/qtwidgets.cpp

#------------------------------------------------------------------------------

%package x11extras
Summary:        PySide x11extras module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description x11extras
PySide x11extras module.

%files x11extras
%{py_platsitedir}/PySide2/QtX11Extras.*.so
%{_datadir}/PySide2/typesystems/typesystem_x11extras*

#------------------------------------------------------------------------------

%if %{with python2}
%package -n python2-pyside2
Summary:	PySide2 for python 2
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core
Requires:	python2-pyside2-gui
Requires:	python2-pyside2-help
Requires:	python2-pyside2-multimedia
Requires:	python2-pyside2-network
Requires:	python2-pyside2-opengl
Requires:	python2-pyside2-script
Requires:	python2-pyside2-scripttools
Requires:	python2-pyside2-sql
Requires:	python2-pyside2-test
Requires:	python2-pyside2-xmlpatterns
Requires:	python2-pyside2-xml
Requires:	python2-pyside2-uitools
Requires:	python2-pyside2-svg
Requires:	python2-pyside2-webengine
Requires:	python2-pyside2-charts
Requires:	python2-pyside2-concurrent
Requires:	python2-pyside2-location
Requires:	python2-pyside2-multimediawidgets
Requires:	python2-pyside2-positioning
Requires:	python2-pyside2-printsupport
Requires:	python2-pyside2-qml
Requires:	python2-pyside2-quick
Requires:	python2-pyside2-quickwidgets
Requires:	python2-pyside2-sensors
Requires:	python2-pyside2-texttospeech
Requires:	python2-pyside2-webchannel
Requires:	python2-pyside2-websockets
Requires:	python2-pyside2-widgets
Requires:	python2-pyside2-x11extras

%description -n python2-pyside2
Pyside2 for python2.

%files -n python2-pyside2

#------------------------------------------------------------------------------

%package -n python2-pyside2-core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description -n python2-pyside2-core
PySide core module.

%files -n python2-pyside2-core
%{py2_platsitedir}/PySide2/QtCore.so
%{py2_platsitedir}/PySide2/__init__.py*
%{py2_platsitedir}/PySide2/_config.py*
%{py2_platsitedir}/PySide2/_git_pyside_version.py*
%{_libdir}/libpyside2%{py2verflags}.so.%{api}*

#------------------------------------------------------------------------------

%package -n python2-pyside2-gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-gui
PySide gui module.

%files -n python2-pyside2-gui
%{py2_platsitedir}/PySide2/QtGui.so
%{_datadir}/PySide2/glue/qtgui.cpp

#------------------------------------------------------------------------------

%package -n python2-pyside2-3d
Summary:	PySide 3D module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-3d
PySide 3D module.

%files -n python2-pyside2-3d
%{py2_platsitedir}/PySide2/Qt3DAnimation.so
%{py2_platsitedir}/PySide2/Qt3DCore.so
%{py2_platsitedir}/PySide2/Qt3DExtras.so
%{py2_platsitedir}/PySide2/Qt3DInput.so
%{py2_platsitedir}/PySide2/Qt3DLogic.so
%{py2_platsitedir}/PySide2/Qt3DRender.so


#------------------------------------------------------------------------------

%package -n python2-pyside2-help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-help
PySide help module.

%files -n python2-pyside2-help
%{py2_platsitedir}/PySide2/QtHelp.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-multimedia
PySide multimedia module.

%files -n python2-pyside2-multimedia
%{py2_platsitedir}/PySide2/QtMultimedia.so


#------------------------------------------------------------------------------

%package -n python2-pyside2-network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-network
PySide network module.

%files -n python2-pyside2-network
%{py2_platsitedir}/PySide2/QtNetwork.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-datavisualization
Summary:	PySide data visualization module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-datavisualization
PySide data visualization module.

%files -n python2-pyside2-datavisualization
%{py2_platsitedir}/PySide2/QtDataVisualization.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-remoteobjects
Summary:	PySide remote objects module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-remoteobjects
PySide remote objects module.

%files -n python2-pyside2-remoteobjects
%{py2_platsitedir}/PySide2/QtRemoteObjects.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-scxml
Summary:	PySide XML Scene Graph module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description -n python2-pyside2-scxml
PySide XML Scene Graph module.

%files -n python2-pyside2-scxml
%{py2_platsitedir}/PySide2/QtScxml.so


#------------------------------------------------------------------------------

%package -n python2-pyside2-opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-opengl
PySide opengl module.

%files -n python2-pyside2-opengl
%{py2_platsitedir}/PySide2/QtOpenGL.so
%{py2_platsitedir}/PySide2/QtOpenGLFunctions.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-script
PySide script module.

%files -n python2-pyside2-script
%{py2_platsitedir}/PySide2/QtScript.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-scripttools
PySide scripttool module.

%files -n python2-pyside2-scripttools
%{py2_platsitedir}/PySide2/QtScriptTools.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-sql
PySide sql module.

%files -n python2-pyside2-sql
%{py2_platsitedir}/PySide2/QtSql.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-svg
PySide svg module.

%files -n python2-pyside2-svg
%{py2_platsitedir}/PySide2/QtSvg.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-test
PySide test module.

%files -n python2-pyside2-test
%{py2_platsitedir}/PySide2/QtTest.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-uitools
PySide uitools module.

%files -n python2-pyside2-uitools
%{py2_platsitedir}/PySide2/QtUiTools.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-webengine
Summary:	PySide webengine module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-webengine
PySide webengine module.

%files -n python2-pyside2-webengine
%{py2_platsitedir}/PySide2/QtWebEngine*.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-xmlpatterns
PySide xmlpatterns module.

%files -n python2-pyside2-xmlpatterns
%{py2_platsitedir}/PySide2/QtXmlPatterns.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-xml
PySide xml module.

%files -n python2-pyside2-xml
%{py2_platsitedir}/PySide2/QtXml.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-charts
Summary:        PySide2 charts module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-charts
PySide2 charts module.

%files -n python2-pyside2-charts
%{py2_platsitedir}/PySide2/QtCharts.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-concurrent
Summary:        PySide2 concurrent module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-concurrent
PySide2 concurrent module.

%files -n python2-pyside2-concurrent
%{py2_platsitedir}/PySide2/QtConcurrent.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-location
Summary:        PySide2 location module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-location
PySide2 location module.

%files -n python2-pyside2-location
%{py2_platsitedir}/PySide2/QtLocation.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-multimediawidgets
Summary:        PySide2 multimediawidgets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-multimediawidgets
PySide2 multimediawidgets module.

%files -n python2-pyside2-multimediawidgets
%{py2_platsitedir}/PySide2/QtMultimediaWidgets.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-positioning
Summary:        PySide2 positioning module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-positioning
PySide2 positioning module.

%files -n python2-pyside2-positioning
%{py2_platsitedir}/PySide2/QtPositioning.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-printsupport
Summary:        PySide2 printsupport module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-printsupport
PySide2 printsupport module.

%files -n python2-pyside2-printsupport
%{py2_platsitedir}/PySide2/QtPrintSupport.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-qml
Summary:        PySide2 qml module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-qml
PySide2 qml module.

%files -n python2-pyside2-qml
%{py2_platsitedir}/PySide2/QtQml.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-quick
Summary:        PySide2 quick module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-quick
PySide2 quick module.

%files -n python2-pyside2-quick
%{py2_platsitedir}/PySide2/QtQuick.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-quickwidgets
Summary:        PySide2 quickwidgets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-quickwidgets
PySide2 quickwidgets module.

%files -n python2-pyside2-quickwidgets
%{py2_platsitedir}/PySide2/QtQuickWidgets.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-sensors
Summary:        PySide2 sensors module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-sensors
PySide2 sensors module.

%files -n python2-pyside2-sensors
%{py2_platsitedir}/PySide2/QtSensors.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-texttospeech
Summary:        PySide2 texttospeech module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-texttospeech
PySide2 texttospeech module.

%files -n python2-pyside2-texttospeech
%{py2_platsitedir}/PySide2/QtTextToSpeech.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-webchannel
Summary:        PySide2 webchannel module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-webchannel
PySide2 webchannel module.

%files -n python2-pyside2-webchannel
%{py2_platsitedir}/PySide2/QtWebChannel.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-websockets
Summary:        PySide2 websockets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-websockets
PySide2 websockets module.

%files -n python2-pyside2-websockets
%{py2_platsitedir}/PySide2/QtWebSockets.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-widgets
Summary:        PySide2 widgets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-widgets
PySide2 widgets module.

%files -n python2-pyside2-widgets
%{py2_platsitedir}/PySide2/QtWidgets.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-x11extras
Summary:        PySide2 x11extras module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-x11extras
PySide2 x11extras module.

%files -n python2-pyside2-x11extras
%{py2_platsitedir}/PySide2/QtX11Extras.so

#------------------------------------------------------------------------------
%endif

%package devel
Summary:	PySide devel files
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}-%{release}
Requires:	shiboken2 = %{EVRD}

%description devel
PySide devel files.

%files devel
%{_bindir}/pyside2-lupdate
%{_bindir}/pyside2-rcc
%{_bindir}/pyside2-uic
%{_bindir}/pyside_tool.py
%{_includedir}/shiboken2
%{_includedir}/PySide2
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*
%{_libdir}/*.so
%{_datadir}/PySide2/glue
%{_datadir}/PySide2/typesystems/glue
%{py_platsitedir}/pyside2uic

#------------------------------------------------------------------------------

%package python2-devel
Summary:	PySide devel files for Python 2.x
Group:		Development/KDE and Qt
Requires:	%{name}-devel = %{version}-%{release}
Requires:	python2-%{name} = %{version}-%{release}

%description python2-devel
PySide devel files for Python 2.x.

%files python2-devel
%{py2_platsitedir}/pyside2uic

#------------------------------------------------------------------------------


%prep
%setup -qn pyside-setup-opensource-src-%{version}
%autopatch -p1

%if %{with python2}
cp -a . %py2dir

pushd %{py2dir}
%cmake_qt5 -DBUILD_TESTS=OFF \
	-DUSE_PYTHON_VERSION=2 \
	-G Ninja
popd
%endif

%cmake_qt5 -DBUILD_TESTS=OFF \
	-DUSE_PYTHON_VERSION=3 \
	-G Ninja

%build
%define Werror_cflags %nil

%if %{with python2}
pushd %{py2dir}
%ninja_build -C build
popd
%endif

%ninja_build -C build


%install
%if %{with python2}
pushd %{py2dir}
%ninja_install -C build
popd
%endif

%ninja_install -C build
python setup.py egg_info
for name in PySide2 shiboken2 shiboken2_generator; do
	mkdir -p %{buildroot}%{py_platsitedir}/$name-%{version}-py3.7.egg-info
	cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
		%{buildroot}%{py_platsitedir}/$name-%{version}-py3.7.egg-info/
done

# icon_cache is not executable and therefore  should not have a shebang
sed -i '/^#!/d' %{buildroot}%{python_sitearch}/pyside2uic/icon_cache.py

# FIXME need to make sure those are actually safe to remove and not
# e.g. read by shiboken while generating bindings for applications
# but for now, it LOOKS safe...
rm -f	%{buildroot}%{_datadir}/PySide2/typesystems/typesystem_core_mac.xml \
	%{buildroot}%{_datadir}/PySide2/typesystems/typesystem_core_win.xml
