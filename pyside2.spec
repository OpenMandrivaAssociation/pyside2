%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define py2verflags -python2.7
%define api 5.11

%define debug_package %{nil}

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt5
Name:		pyside2
Version:	5.11.2
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
Source0:	https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-everywhere-src-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(python2)
BuildRequires:  python2-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:  python-setuptools 
BuildRequires:	python-sphinx
Requires:	python-shiboken2
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

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files

#------------------------------------------------------------------------------

%package core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description core
PySide core module.

%files core
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/PySide2/QtCore.*.so
%{py_platsitedir}/PySide2/__init__.py
%{py_platsitedir}/PySide2/_config.py
%{py_platsitedir}/PySide2/_git_pyside_version.py
%{py_platsitedir}/PySide2/typesystems/typesystem_core*
%{py_platsitedir}/PySide2/typesystems/typesystem_templates.*
%{py_platsitedir}/PySide2/libpyside2.%{py3verflags}.so.%{api}*
%{py_platsitedir}/PySide2/support

#------------------------------------------------------------------------------

%package gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description gui
PySide gui module.

%files gui
%{py_platsitedir}/PySide2/QtGui.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_gui*

#------------------------------------------------------------------------------

%package help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description help
PySide help module.

%files help
%{py_platsitedir}/PySide2/QtHelp.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_help.*

#------------------------------------------------------------------------------

%package multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description multimedia
PySide multimedia module.

%files multimedia
%{py_platsitedir}/PySide2/QtMultimedia.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_multimedia.xml
%{py_platsitedir}/PySide2/typesystems/typesystem_multimedia_*

#------------------------------------------------------------------------------

%package network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description network
PySide network module.

%files network
%{py_platsitedir}/PySide2/QtNetwork.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_network.*

#------------------------------------------------------------------------------

%package opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description opengl
PySide opengl module.

%files opengl
%{py_platsitedir}/PySide2/QtOpenGL.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_opengl*

#------------------------------------------------------------------------------

%package script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description script
PySide script module.

%files script
%{py_platsitedir}/PySide2/QtScript.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_script.*

#------------------------------------------------------------------------------

%package scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description scripttools
PySide scripttool module.

%files scripttools
%{py_platsitedir}/PySide2/QtScriptTools.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_scripttools.*

#------------------------------------------------------------------------------

%package sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description sql
PySide sql module.

%files sql
%{py_platsitedir}/PySide2/QtSql.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_sql.*

#------------------------------------------------------------------------------

%package svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description svg
PySide svg module.

%files svg
%{py_platsitedir}/PySide2/QtSvg.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_svg.*

#------------------------------------------------------------------------------

%package test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description test
PySide test module.

%files test
%{py_platsitedir}/PySide2/QtTest.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_test.*

#------------------------------------------------------------------------------

%package uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description uitools
PySide uitools module.

%files uitools
%{py_platsitedir}/PySide2/QtUiTools.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_uitools.*

#------------------------------------------------------------------------------

%package webengine
Summary:	PySide webengine module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description webengine
PySide webengine module.

%files webengine
%{py_platsitedir}/PySide2/QtWebEngine*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_webengine*

#------------------------------------------------------------------------------

%package xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description xmlpatterns
PySide xmlpatterns module.

%files xmlpatterns
%{py_platsitedir}/PySide2/QtXmlPatterns.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_xmlpatterns*

#------------------------------------------------------------------------------

%package xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description xml
PySide xml module.

%files xml
%{py_platsitedir}/PySide2/QtXml.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_xml.*

#------------------------------------------------------------------------------

%package charts
Summary:        PySide charts module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description charts
PySide charts module.

%files charts
%{py_platsitedir}/PySide2/QtCharts.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_charts*

#------------------------------------------------------------------------------

%package concurrent
Summary:        PySide concurrent module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description concurrent
PySide concurrent module.

%files concurrent
%{py_platsitedir}/PySide2/QtConcurrent.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_concurrent*

#------------------------------------------------------------------------------

%package location
Summary:        PySide location module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description location
PySide location module.

%files location
%{py_platsitedir}/PySide2/QtLocation.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_location*

#------------------------------------------------------------------------------

%package multimediawidgets
Summary:        PySide multimediawidgets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description multimediawidgets
PySide multimediawidgets module.

%files multimediawidgets
%{py_platsitedir}/PySide2/QtMultimediaWidgets.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_multimediawidgets*

#------------------------------------------------------------------------------

%package positioning
Summary:        PySide positioning module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description positioning
PySide positioning module.

%files positioning
%{py_platsitedir}/PySide2/QtPositioning.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_positioning*

#------------------------------------------------------------------------------

%package printsupport
Summary:        PySide printsupport module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description printsupport
PySide printsupport module.

%files printsupport
%{py_platsitedir}/PySide2/QtPrintSupport.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_printsupport*

#------------------------------------------------------------------------------

%package qml
Summary:        PySide qml module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description qml
PySide qml module.

%files qml
%{py_platsitedir}/PySide2/QtQml.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_qml*

#------------------------------------------------------------------------------

%package quick
Summary:        PySide quick module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description quick
PySide quick module.

%files quick
%{py_platsitedir}/PySide2/QtQuick.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_quick.xml

#------------------------------------------------------------------------------

%package quickwidgets
Summary:        PySide quickwidgets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description quickwidgets
PySide quickwidgets module.

%files quickwidgets
%{py_platsitedir}/PySide2/QtQuickWidgets.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_quickwidgets*

#------------------------------------------------------------------------------

%package sensors
Summary:        PySide sensors module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description sensors
PySide sensors module.

%files sensors
%{py_platsitedir}/PySide2/QtSensors.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_sensors*

#------------------------------------------------------------------------------

%package texttospeech
Summary:        PySide texttospeech module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description texttospeech
PySide texttospeech module.

%files texttospeech
%{py_platsitedir}/PySide2/QtTextToSpeech.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_texttospeech*

#------------------------------------------------------------------------------

%package webchannel
Summary:        PySide webchannel module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description webchannel
PySide webchannel module.

%files webchannel
%{py_platsitedir}/PySide2/QtWebChannel.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_webchannel*

#------------------------------------------------------------------------------

%package websockets
Summary:        PySide websockets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description websockets
PySide websockets module.

%files websockets
%{py_platsitedir}/PySide2/QtWebSockets.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_websockets*

#------------------------------------------------------------------------------

%package widgets
Summary:        PySide widgets module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description widgets
PySide widgets module.

%files widgets
%{py_platsitedir}/PySide2/QtWidgets.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_widgets*

#------------------------------------------------------------------------------

%package x11extras
Summary:        PySide x11extras module
Group:          Development/KDE and Qt
Requires:       pyside2-core = %{version}

%description x11extras
PySide x11extras module.

%files x11extras
%{py_platsitedir}/PySide2/QtX11Extras.*.so
%{py_platsitedir}/PySide2/typesystems/typesystem_x11extras*

#------------------------------------------------------------------------------

%package -n python-shiboken2
Summary:        PySide shiboken2 module
Group:          Development/KDE and Qt

%description -n python-shiboken2
PySide shiboken2 module.

%files -n python-shiboken2
%{py_platsitedir}/PySide2/libshiboken2.*
%{py_platsitedir}/PySide2/shiboken2*

#------------------------------------------------------------------------------

%package -n python2-pyside2
Requires:	python-shiboken2
Requires:       python2-pyside2-core
Requires:       python2-pyside2-gui
Requires:       python2-pyside2-help
Requires:       python2-pyside2-multimedia
Requires:       python2-pyside2-network
Requires:       python2-pyside2-opengl
Requires:       python2-pyside2-script
Requires:       python2-pyside2-scripttools
Requires:       python2-pyside2-sql
Requires:       python2-pyside2-test
Requires:       python2-pyside2-xmlpatterns
Requires:       python2-pyside2-xml
Requires:       python2-pyside2-uitools
Requires:       python2-pyside2-svg
Requires:       python2-pyside2-webengine
Requires:	python2-pyside2-charts
Requires:	python2-pyside2-concurrent
Requires:	python2-pyside2-location
Requires: 	python2-pyside2-multimediawidgets
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
%{py2_platsitedir}/*.egg-info
%{py2_platsitedir}/PySide2/QtCore.so
%{py2_platsitedir}/PySide2/__init__.py
%{py2_platsitedir}/PySide2/_config.py
%{py2_platsitedir}/PySide2/_git_pyside_version.py
%{py2_platsitedir}/PySide2/libpyside2%{py2verflags}.so.%{api}*
%{py2_platsitedir}/PySide2/typesystems/typesystem_core*
%{py2_platsitedir}/PySide2/typesystems/typesystem_templates.*
%{py2_platsitedir}/PySide2/support

#------------------------------------------------------------------------------

%package -n python2-pyside2-gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-gui
PySide gui module.

%files -n python2-pyside2-gui
%{py2_platsitedir}/PySide2/QtGui.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_gui*

#------------------------------------------------------------------------------

%package -n python2-pyside2-help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-help
PySide help module.

%files -n python2-pyside2-help
%{py2_platsitedir}/PySide2/QtHelp.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_help.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-multimedia
PySide multimedia module.

%files -n python2-pyside2-multimedia
%{py2_platsitedir}/PySide2/QtMultimedia.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_multimedia.xml
%{py2_platsitedir}/PySide2/typesystems/typesystem_multimedia_*


#------------------------------------------------------------------------------

%package -n python2-pyside2-network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-network
PySide network module.

%files -n python2-pyside2-network
%{py2_platsitedir}/PySide2/QtNetwork.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_network.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-opengl
PySide opengl module.

%files -n python2-pyside2-opengl
%{py2_platsitedir}/PySide2/QtOpenGL.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_opengl*

#------------------------------------------------------------------------------

%package -n python2-pyside2-script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-script
PySide script module.

%files -n python2-pyside2-script
%{py2_platsitedir}/PySide2/QtScript.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_script.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-scripttools
PySide scripttool module.

%files -n python2-pyside2-scripttools
%{py2_platsitedir}/PySide2/QtScriptTools.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_scripttools.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-sql
PySide sql module.

%files -n python2-pyside2-sql
%{py2_platsitedir}/PySide2/QtSql.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_sql.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-svg
PySide svg module.

%files -n python2-pyside2-svg
%{py2_platsitedir}/PySide2/QtSvg.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_svg.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-test
PySide test module.

%files -n python2-pyside2-test
%{py2_platsitedir}/PySide2/QtTest.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_test.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-uitools
PySide uitools module.

%files -n python2-pyside2-uitools
%{py2_platsitedir}/PySide2/QtUiTools.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_uitools.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-webengine
Summary:	PySide webengine module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-webengine
PySide webengine module.

%files -n python2-pyside2-webengine
%{py2_platsitedir}/PySide2/QtWebEngine*.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_webengine*

#------------------------------------------------------------------------------

%package -n python2-pyside2-xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-xmlpatterns
PySide xmlpatterns module.

%files -n python2-pyside2-xmlpatterns
%{py2_platsitedir}/PySide2/QtXmlPatterns.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_xmlpatterns*

#------------------------------------------------------------------------------

%package -n python2-pyside2-xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-xml
PySide xml module.

%files -n python2-pyside2-xml
%{py2_platsitedir}/PySide2/QtXml.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_xml.*

#------------------------------------------------------------------------------

%package -n python2-pyside2-charts
Summary:        PySide2 charts module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-charts
PySide2 charts module.

%files -n python2-pyside2-charts
%{py2_platsitedir}/PySide2/QtCharts.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_charts*

#------------------------------------------------------------------------------

%package -n python2-pyside2-concurrent
Summary:        PySide2 concurrent module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-concurrent
PySide2 concurrent module.

%files -n python2-pyside2-concurrent
%{py2_platsitedir}/PySide2/QtConcurrent.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_concurrent*

#------------------------------------------------------------------------------

%package -n python2-pyside2-location
Summary:        PySide2 location module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-location
PySide2 location module.

%files -n python2-pyside2-location
%{py2_platsitedir}/PySide2/QtLocation.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_location*

#------------------------------------------------------------------------------

%package -n python2-pyside2-multimediawidgets
Summary:        PySide2 multimediawidgets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-multimediawidgets
PySide2 multimediawidgets module.

%files -n python2-pyside2-multimediawidgets
%{py2_platsitedir}/PySide2/QtMultimediaWidgets.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_multimediawidgets*

#------------------------------------------------------------------------------

%package -n python2-pyside2-positioning
Summary:        PySide2 positioning module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-positioning
PySide2 positioning module.

%files -n python2-pyside2-positioning
%{py2_platsitedir}/PySide2/QtPositioning.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_positioning*

#------------------------------------------------------------------------------

%package -n python2-pyside2-printsupport
Summary:        PySide2 printsupport module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-printsupport
PySide2 printsupport module.

%files -n python2-pyside2-printsupport
%{py2_platsitedir}/PySide2/QtPrintSupport.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_printsupport*

#------------------------------------------------------------------------------

%package -n python2-pyside2-qml
Summary:        PySide2 qml module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-qml
PySide2 qml module.

%files -n python2-pyside2-qml
%{py2_platsitedir}/PySide2/QtQml.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_qml*

#------------------------------------------------------------------------------

%package -n python2-pyside2-quick
Summary:        PySide2 quick module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-quick
PySide2 quick module.

%files -n python2-pyside2-quick
%{py2_platsitedir}/PySide2/QtQuick.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_quick.xml

#------------------------------------------------------------------------------

%package -n python2-pyside2-quickwidgets
Summary:        PySide2 quickwidgets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-quickwidgets
PySide2 quickwidgets module.

%files -n python2-pyside2-quickwidgets
%{py2_platsitedir}/PySide2/QtQuickWidgets.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_quickwidgets*

#------------------------------------------------------------------------------

%package -n python2-pyside2-sensors
Summary:        PySide2 sensors module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-sensors
PySide2 sensors module.

%files -n python2-pyside2-sensors
%{py2_platsitedir}/PySide2/QtSensors.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_sensors*

#------------------------------------------------------------------------------

%package -n python2-pyside2-texttospeech
Summary:        PySide2 texttospeech module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-texttospeech
PySide2 texttospeech module.

%files -n python2-pyside2-texttospeech
%{py2_platsitedir}/PySide2/QtTextToSpeech.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_texttospeech*

#------------------------------------------------------------------------------

%package -n python2-pyside2-webchannel
Summary:        PySide2 webchannel module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-webchannel
PySide2 webchannel module.

%files -n python2-pyside2-webchannel
%{py2_platsitedir}/PySide2/QtWebChannel.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_webchannel*

#------------------------------------------------------------------------------

%package -n python2-pyside2-websockets
Summary:        PySide2 websockets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-websockets
PySide2 websockets module.

%files -n python2-pyside2-websockets
%{py2_platsitedir}/PySide2/QtWebSockets.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_websockets*

#------------------------------------------------------------------------------

%package -n python2-pyside2-widgets
Summary:        PySide2 widgets module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-widgets
PySide2 widgets module.

%files -n python2-pyside2-widgets
%{py2_platsitedir}/PySide2/QtWidgets.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_widgets*

#------------------------------------------------------------------------------

%package -n python2-pyside2-x11extras
Summary:        PySide2 x11extras module
Group:          Development/KDE and Qt
Requires:       python2-pyside2-core = %{version}

%description -n python2-pyside2-x11extras
PySide2 x11extras module.

%files -n python2-pyside2-x11extras
%{py2_platsitedir}/PySide2/QtX11Extras.so
%{py2_platsitedir}/PySide2/typesystems/typesystem_x11extras*

#------------------------------------------------------------------------------

%package -n python2-shiboken2
Summary:        PySide shiboken2 module
Group:          Development/KDE and Qt

%description -n python2-shiboken2
PySide shiboken2 module.

%files -n python2-shiboken2
%{py2_platsitedir}/PySide2/libshiboken2*
%{py2_platsitedir}/PySide2/shiboken2*

#------------------------------------------------------------------------------


%package devel
Summary:        PySide devel files
Group:          Development/KDE and Qt
Requires:       %{name} = %{version}-%{release}
Requires:       python2-%{name} = %{version}-%{release}

%description devel
PySide devel files.

%files devel
%{py2_platsitedir}/pyside2uic
%{py2_platsitedir}/PySide2/pyside2-rcc
%{py2_platsitedir}/PySide2/pyside2-lupdate
%{py2_platsitedir}/PySide2/include
%{py2_platsitedir}/PySide2/examples
%{py2_platsitedir}/PySide2/scripts
%{py2_platsitedir}/PySide2/docs
%{py3_platsitedir}/pyside2uic
%{py3_platsitedir}/PySide2/pyside2-rcc
%{py3_platsitedir}/PySide2/pyside2-lupdate
%{py3_platsitedir}/PySide2/include
%{py3_platsitedir}/PySide2/examples
%{py3_platsitedir}/PySide2/scripts
%{py3_platsitedir}/PySide2/docs
%{_bindir}/pyside2-uic

#------------------------------------------------------------------------------


%prep
%setup -qn pyside-setup-everywhere-src-%{version}

cp -a . %py2dir

%build

RPM_BUILD_NCPUS=$(/usr/bin/getconf _NPROCESSORS_ONLN)

%define Werror_cflags %nil
pushd %{py2dir}
%__python2 setup.py build --jobs=$RPM_BUILD_NCPUS
popd
%__python setup.py build --jobs=$RPM_BUILD_NCPUS

%install
pushd %{py2dir}
%__python2 setup.py install --skip-build --root=%{buildroot}
popd

%__python setup.py install --skip-build --root=%{buildroot}
