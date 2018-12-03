%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define py2verflags -python2.7

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt5
Name:		pyside2
Version:	5.11.2
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
Source0:	https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-everywhere-src-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(python2)
BuildRequires:  python2-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:  python-setuptools 
BuildRequires:	python-sphinx
Requires:	pyside2-phonon
Requires:	pyside2-core
Requires:	pyside2-declarative
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
Requires:	pyside2-webkit

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files

#------------------------------------------------------------------------------

%package phonon
Summary:	PySide phonon module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description phonon
PySide phonon module.

%files phonon
%{py_platsitedir}/PySide/phonon.so
%{_datadir}/PySide/typesystems/typesystem_phonon.*

#------------------------------------------------------------------------------

%package core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description core
PySide core module.

%files core
%{py_platsitedir}/PySide/QtCore.so
%{py_platsitedir}/PySide/__init__.py
%{py_platsitedir}/PySide/_utils.py
%{_datadir}/PySide/typesystems/typesystem_core*
%{_datadir}/PySide/typesystems/typesystem_templates.*

#------------------------------------------------------------------------------

%package declarative
Summary:	PySide declarative module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description declarative
PySide declarative module.

%files declarative
%{py_platsitedir}/PySide/QtDeclarative.so
%{_datadir}/PySide/typesystems/typesystem_declarative.*

#------------------------------------------------------------------------------

%package gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description gui
PySide gui module.

%files gui
%{py_platsitedir}/PySide/QtGui.so
%{_datadir}/PySide/typesystems/typesystem_gui*

#------------------------------------------------------------------------------

%package help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description help
PySide help module.

%files help
%{py_platsitedir}/PySide/QtHelp.so
%{_datadir}/PySide/typesystems/typesystem_help.*

#------------------------------------------------------------------------------

%package multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description multimedia
PySide multimedia module.

%files multimedia
%{py_platsitedir}/PySide/QtMultimedia.so
%{_datadir}/PySide/typesystems/typesystem_multimedia*

#------------------------------------------------------------------------------

%package network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description network
PySide network module.

%files network
%{py_platsitedir}/PySide/QtNetwork.so
%{_datadir}/PySide/typesystems/typesystem_network.*

#------------------------------------------------------------------------------

%package opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description opengl
PySide opengl module.

%files opengl
%{py_platsitedir}/PySide/QtOpenGL.so
%{_datadir}/PySide/typesystems/typesystem_opengl*

#------------------------------------------------------------------------------

%package script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description script
PySide script module.

%files script
%{py_platsitedir}/PySide/QtScript.so
%{_datadir}/PySide/typesystems/typesystem_script.*

#------------------------------------------------------------------------------

%package scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description scripttools
PySide scripttool module.

%files scripttools
%{py_platsitedir}/PySide/QtScriptTools.so
%{_datadir}/PySide/typesystems/typesystem_scripttools.*

#------------------------------------------------------------------------------

%package sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description sql
PySide sql module.

%files sql
%{py_platsitedir}/PySide/QtSql.so
%{_datadir}/PySide/typesystems/typesystem_sql.*

#------------------------------------------------------------------------------

%package svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description svg
PySide svg module.

%files svg
%{py_platsitedir}/PySide/QtSvg.so
%{_datadir}/PySide/typesystems/typesystem_svg.*

#------------------------------------------------------------------------------

%package test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description test
PySide test module.

%files test
%{py_platsitedir}/PySide/QtTest.so
%{_datadir}/PySide/typesystems/typesystem_test.*

#------------------------------------------------------------------------------

%package uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description uitools
PySide uitools module.

%files uitools
%{py_platsitedir}/PySide/QtUiTools.so
%{_datadir}/PySide/typesystems/typesystem_uitools.*

#------------------------------------------------------------------------------

%package webkit
Summary:	PySide webkit module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description webkit
PySide webkit module.

%files webkit
%{py_platsitedir}/PySide/QtWebKit.so
%{_datadir}/PySide/typesystems/typesystem_webkit*

#------------------------------------------------------------------------------

%package xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description xmlpatterns
PySide xmlpatterns module.

%files xmlpatterns
%{py_platsitedir}/PySide/QtXmlPatterns.so
%{_datadir}/PySide/typesystems/typesystem_xmlpatterns*

#------------------------------------------------------------------------------

%package xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	pyside2-core = %{version}

%description xml
PySide xml module.

%files xml
%{py_platsitedir}/PySide/QtXml.so
%{_datadir}/PySide/typesystems/typesystem_xml.*

#------------------------------------------------------------------------------

%define api 1.2
%define libname %mklibname pyside.%{py3verflags} %{api}

%package -n %{libname}
Summary:	PySide core library
Group:		Development/KDE and Qt
Obsoletes:	%{_lib}pyside1 < 1.1.2-2

%description -n %{libname}
PySide core library.

%files -n %{libname}
%{_libdir}/libpyside.%{py3verflags}.so.%{api}*


#------------------------------------------------------------------------------

%define api 1.2
%define libname_py2 %mklibname pyside%{py2verflags} %{api}

%package -n %{libname_py2}
Summary:        PySide core library
Group:          Development/KDE and Qt

%description -n %{libname_py2}
PySide core library.

%files -n %{libname_py2}
%{_libdir}/libpyside%{py2verflags}.so.%{api}*

#------------------------------------------------------------------------------

%package -n python2-pyside
Requires:       python2-pyside2-phonon
Requires:       python2-pyside2-core
Requires:       python2-pyside2-declarative
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
Requires:       python2-pyside2-webkit

%description -n python2-pyside
Pyside for python2.

%files -n python2-pyside

#------------------------------------------------------------------------------

%package -n python2-pyside2-phonon
Summary:	PySide phonon module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-phonon
PySide phonon module.

%files -n python2-pyside2-phonon
%{py2_platsitedir}/PySide/phonon.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description -n python2-pyside2-core
PySide core module.

%files -n python2-pyside2-core
%{py2_platsitedir}/PySide/QtCore.so
%{py2_platsitedir}/PySide/__init__.py
%{py2_platsitedir}/PySide/_utils.py

#------------------------------------------------------------------------------

%package -n python2-pyside2-declarative
Summary:	PySide declarative module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-declarative
PySide declarative module.

%files -n python2-pyside2-declarative
%{py2_platsitedir}/PySide/QtDeclarative.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-gui
PySide gui module.

%files -n python2-pyside2-gui
%{py2_platsitedir}/PySide/QtGui.so
#------------------------------------------------------------------------------

%package -n python2-pyside2-help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-help
PySide help module.

%files -n python2-pyside2-help
%{py2_platsitedir}/PySide/QtHelp.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-multimedia
PySide multimedia module.

%files -n python2-pyside2-multimedia
%{py2_platsitedir}/PySide/QtMultimedia.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-network
PySide network module.

%files -n python2-pyside2-network
%{py2_platsitedir}/PySide/QtNetwork.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-opengl
PySide opengl module.

%files -n python2-pyside2-opengl
%{py2_platsitedir}/PySide/QtOpenGL.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-script
PySide script module.

%files -n python2-pyside2-script
%{py2_platsitedir}/PySide/QtScript.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-scripttools
PySide scripttool module.

%files -n python2-pyside2-scripttools
%{py2_platsitedir}/PySide/QtScriptTools.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-sql
PySide sql module.

%files -n python2-pyside2-sql
%{py2_platsitedir}/PySide/QtSql.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-svg
PySide svg module.

%files -n python2-pyside2-svg
%{py2_platsitedir}/PySide/QtSvg.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-test
PySide test module.

%files -n python2-pyside2-test
%{py2_platsitedir}/PySide/QtTest.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-uitools
PySide uitools module.

%files -n python2-pyside2-uitools
%{py2_platsitedir}/PySide/QtUiTools.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-webkit
Summary:	PySide webkit module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-webkit
PySide webkit module.

%files -n python2-pyside2-webkit
%{py2_platsitedir}/PySide/QtWebKit.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-xmlpatterns
PySide xmlpatterns module.

%files -n python2-pyside2-xmlpatterns
%{py2_platsitedir}/PySide/QtXmlPatterns.so

#------------------------------------------------------------------------------

%package -n python2-pyside2-xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	python2-pyside2-core = %{version}

%description -n python2-pyside2-xml
PySide xml module.

%files -n python2-pyside2-xml
%{py2_platsitedir}/PySide/QtXml.so

#------------------------------------------------------------------------------

%package devel
Summary:        PySide devel files
Group:          Development/KDE and Qt
Requires:       %{name} = %{version}-%{release}
Requires:       python2-%{name} = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libname_py2} = %{version}-%{release}

%description devel
PySide devel files.

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*


#------------------------------------------------------------------------------


%prep
%setup -qn pyside-setup-everywhere-src-%{version}

cp -a . %py2dir

%build

%define Werror_cflags %nil
pushd %{py2dir}
%__python2 setup.py build
popd
%__python setup.py build
%make

%install
pushd %{py2dir}
%makeinstall_std -C build
popd

%makeinstall_std -C build
