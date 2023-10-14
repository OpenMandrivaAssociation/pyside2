%define _disable_ld_no_undefined 1

%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define api %(echo %{version} |cut -d. -f1-2)

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt5
Name:		pyside2
Version:	5.15.11
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
Source0:	https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-opensource-src-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
Patch0:		pyside-5.15.2-dont-use-unrecognized-option.patch
# (fedora)
Patch1:		https://src.fedoraproject.org/rpms/python-pyside2/raw/rawhide/f/pyside2-tools-obsolete.patch
Patch2:		https://src.fedoraproject.org/rpms/python-pyside2/raw/rawhide/f/python-pyside2-options_py.patch
Patch5:		https://raw.githubusercontent.com/NixOS/nixpkgs/master/pkgs/development/python-modules/shiboken2/nix_compile_cflags.patch
Patch6:		https://src.fedoraproject.org/rpms/python-pyside2/raw/rawhide/f/build-tests.patch
BuildRequires:	cmake(ECM)
BuildRequires:	python3dist(numpy)
BuildRequires:	clang-devel
BuildRequires:	llvm-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	cmake(Qt5Bluetooth)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5Enginio)
BuildRequires:	cmake(Qt5Nfc)
BuildRequires:	cmake(Qt5Positioning)
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
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5SerialPort)
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
BuildRequires:	cmake(Qt5Location)

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
BuildRequires:	python3dist(wheel)
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
Requires:	pyside2-quickcontrols
Requires:	pyside2-quickwidgets
Requires:	pyside2-serialport
Requires:	pyside2-sensors
Requires:	pyside2-texttospeech
Requires:	pyside2-webchannel
Requires:	pyside2-websockets
Requires:	pyside2-widgets
Requires:	pyside2-x11extras
# cmake files act up when running into obsolete-ish Qt5Declarative
BuildConflicts:	pkgconfig(Qt5Declarative)

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
%doc %{_mandir}/man1/*
%{py_platsitedir}/shiboken2-%{version}-py%{py_ver}.egg-info
%{py_platsitedir}/shiboken2_generator-%{version}-py%{py_ver}.egg-info

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
%{_libdir}/libpyside2.%{py3verflags}.so.%{api}*
%dir %{_datadir}/PySide2/glue
%{_datadir}/PySide2/glue/qtcore.cpp
%dir %{_datadir}/PySide2/typesystems
%{_datadir}/PySide2/typesystems/typesystem_core.xml
%{_datadir}/PySide2/typesystems/typesystem_core_x11.xml
%{_datadir}/PySide2/typesystems/*_common.xml
%{py_platsitedir}/PySide2-%{version}-py%{py_ver}.egg-info

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
Requires:	pyside2-core = %{version}

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
Summary:	PySide charts module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description charts
PySide charts module.

%files charts
%{py_platsitedir}/PySide2/QtCharts.*.so
%{_datadir}/PySide2/typesystems/typesystem_charts*

#------------------------------------------------------------------------------

%package concurrent
Summary:	PySide concurrent module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description concurrent
PySide concurrent module.

%files concurrent
%{py_platsitedir}/PySide2/QtConcurrent.*.so
%{_datadir}/PySide2/typesystems/typesystem_concurrent*

#------------------------------------------------------------------------------

%package location
Summary:	PySide location module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description location
PySide location module.

%files location
%{py_platsitedir}/PySide2/QtLocation.*.so
%{_datadir}/PySide2/typesystems/typesystem_location*

#------------------------------------------------------------------------------

%package multimediawidgets
Summary:	PySide multimediawidgets module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description multimediawidgets
PySide multimediawidgets module.

%files multimediawidgets
%{py_platsitedir}/PySide2/QtMultimediaWidgets.*.so
%{_datadir}/PySide2/typesystems/typesystem_multimediawidgets*

#------------------------------------------------------------------------------

%package positioning
Summary:	PySide positioning module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description positioning
PySide positioning module.

%files positioning
%{py_platsitedir}/PySide2/QtPositioning.*.so
%{_datadir}/PySide2/typesystems/typesystem_positioning*

#------------------------------------------------------------------------------

%package printsupport
Summary:	PySide printsupport module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description printsupport
PySide printsupport module.

%files printsupport
%{py_platsitedir}/PySide2/QtPrintSupport.*.so
%{_datadir}/PySide2/typesystems/typesystem_printsupport*
%{_datadir}/PySide2/glue/qtprintsupport.cpp

#------------------------------------------------------------------------------

%package qml
Summary:	PySide qml module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description qml
PySide qml module.

%files qml
%{py_platsitedir}/PySide2/QtQml.*.so
%{_datadir}/PySide2/typesystems/typesystem_qml*
%{_datadir}/PySide2/glue/qtqml.cpp

#------------------------------------------------------------------------------

%package quick
Summary:	PySide quick module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description quick
PySide quick module.

%files quick
%{py_platsitedir}/PySide2/QtQuick.*.so
%{_datadir}/PySide2/typesystems/typesystem_quick.xml
%{_datadir}/PySide2/glue/qtquick.cpp

#------------------------------------------------------------------------------

%package quickwidgets
Summary:	PySide quickwidgets module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description quickwidgets
PySide quickwidgets module.

%files quickwidgets
%{py_platsitedir}/PySide2/QtQuickWidgets.*.so
%{_datadir}/PySide2/typesystems/typesystem_quickwidgets*

#------------------------------------------------------------------------------

%package sensors
Summary:	PySide sensors module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description sensors
PySide sensors module.

%files sensors
%{py_platsitedir}/PySide2/QtSensors.*.so
%{_datadir}/PySide2/typesystems/typesystem_sensors*

#------------------------------------------------------------------------------

%package texttospeech
Summary:	PySide texttospeech module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description texttospeech
PySide texttospeech module.

%files texttospeech
%{py_platsitedir}/PySide2/QtTextToSpeech.*.so
%{_datadir}/PySide2/typesystems/typesystem_texttospeech*

#------------------------------------------------------------------------------

%package webchannel
Summary:	PySide webchannel module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description webchannel
PySide webchannel module.

%files webchannel
%{py_platsitedir}/PySide2/QtWebChannel.*.so
%{_datadir}/PySide2/typesystems/typesystem_webchannel*

#------------------------------------------------------------------------------

%package websockets
Summary:	PySide websockets module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description websockets
PySide websockets module.

%files websockets
%{py_platsitedir}/PySide2/QtWebSockets.*.so
%{_datadir}/PySide2/typesystems/typesystem_websockets*

#------------------------------------------------------------------------------

%package widgets
Summary:	PySide widgets module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description widgets
PySide widgets module.

%files widgets
%{py_platsitedir}/PySide2/QtWidgets.*.so
%{_datadir}/PySide2/typesystems/typesystem_widgets*
%{_datadir}/PySide2/glue/qtwidgets.cpp

#------------------------------------------------------------------------------

%package quickcontrols
Summary:	PySide QtQuick Controls module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description quickcontrols
PySide QtQuick Controls module.

%files quickcontrols
%{py_platsitedir}/PySide2/QtQuickControls2.*.so
%{_datadir}/PySide2/typesystems/typesystem_quickcontrols2.xml

#------------------------------------------------------------------------------

%package serialport
Summary:	PySide serial port module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description serialport
PySide serial port module.

%files serialport
%{py_platsitedir}/PySide2/QtSerialPort.*.so
%{_datadir}/PySide2/typesystems/typesystem_serialport.xml

#------------------------------------------------------------------------------

%package x11extras
Summary:	PySide x11extras module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description x11extras
PySide x11extras module.

%files x11extras
%{py_platsitedir}/PySide2/QtX11Extras.*.so
%{_datadir}/PySide2/typesystems/typesystem_x11extras*

#------------------------------------------------------------------------------
%package devel
Summary:	PySide devel files
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}-%{release}
Requires:	shiboken2 = %{EVRD}

%description devel
PySide devel files.

%files devel
%{_bindir}/pyside2-lupdate
%{_bindir}/pyside2-designer
%{_bindir}/pyside_tool.py
%{_includedir}/shiboken2
%{_includedir}/PySide2
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*
%{_libdir}/*.so
%{_datadir}/PySide2/glue
%{_datadir}/PySide2/typesystems/glue

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n pyside-setup-opensource-src-%{version}
%cmake_qt5 -DBUILD_TESTS=OFF \
	-DUSE_PYTHON_VERSION=3 \
	-G Ninja

%build
%define Werror_cflags %nil
%ninja_build -C build

%install
%ninja_install -C build
python setup.py egg_info
for name in PySide2 shiboken2 shiboken2_generator; do
	mkdir -p %{buildroot}%{py_platsitedir}/$name-%{version}-py%{py_ver}.egg-info
	cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
		%{buildroot}%{py_platsitedir}/$name-%{version}-py%{py_ver}.egg-info/
done

# Let's not conflict with regular (C++) Qt...
cd %{buildroot}%{_bindir}
# We used to need rcc and uic here too... What happened to them?
for i in designer; do
	mv $i pyside2-${i}
done

# FIXME need to make sure those are actually safe to remove and not
# e.g. read by shiboken while generating bindings for applications
# but for now, it LOOKS safe...
rm -f	%{buildroot}%{_datadir}/PySide2/typesystems/typesystem_core_mac.xml \
	%{buildroot}%{_datadir}/PySide2/typesystems/typesystem_core_win.xml
