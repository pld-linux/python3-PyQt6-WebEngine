
%define		module	PyQt6-WebEngine
# minimal required sip version
%define		sip_ver	6.9
# last qt version covered by these bindings (minimal required is currently 6.0.0)
# see sip/QtWebEngineCore/QtWebEngineCoremod.sip /%Timeline
%define		qt_ver	%{version}

Summary:	Python bindings for the Qt6WebEngine module
Summary(pl.UTF-8):	Wiązania Pythona do modułu Qt6WebEngine
Name:		python3-%{module}
Version:	6.9.0
Release:	2
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyqt6-webengine/
Source0:	https://files.pythonhosted.org/packages/source/p/pyqt6-webengine/pyqt6_webengine-%{version}.tar.gz
# Source0-md5:	01baa50f50337ada6d2bbf542c12caf2
URL:		https://www.riverbankcomputing.com/software/pyqtwebengine/
BuildRequires:	Qt6WebEngine-devel >= %{qt_ver}
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt-builder >= 1.17
BuildRequires:	python3-PyQt-builder < 2
BuildRequires:	python3-PyQt6 >= 6.2.0
BuildRequires:	python3-PyQt6-devel >= 6.2.0
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sip6 >= %{sip_ver}
Requires:	Qt6WebEngine >= %{qt_ver}
Requires:	python3-libs >= 1:3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Python bindings for the Qt6WebEngine module.

%description -l pl.UTF-8
Wiązania Pythona do modułu Qt6WebEngine.

%package devel
Summary:	SIP files needed to build bindings for Qt6WebEngine
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania wiązań do Qt6WebEngine
Group:		Development/Languages/Python
Requires:	python3-PyQt6-devel >= 6.2.0
Requires:	sip6 >= %{sip_ver}
Obsoletes:	sip-PyQt6-WebEngine < 6.9.0-2

%description devel
SIP files needed to build bindings for Qt6WebEngine.

%description devel -l pl.UTF-8
Pliki SIP potrzebne do budowania wiązań do Qt6WebEngine.

%prep
%setup -q -n pyqt6_webengine-%{version}

%build
sip-build --build-dir build-py3 \
	--jobs %{__jobs} \
	--verbose \
	--pep484-pyi \
	--qmake="%{_bindir}/qmake-qt6" \
	--scripts-dir=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-py3 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtWebEngineCore.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtWebEngineQuick.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt6/QtWebEngineWidgets.abi3.so
%{py3_sitedir}/PyQt6/QtWebEngineCore.pyi
%{py3_sitedir}/PyQt6/QtWebEngineQuick.pyi
%{py3_sitedir}/PyQt6/QtWebEngineWidgets.pyi
%{py3_sitedir}/pyqt6_webengine-%{version}.dist-info

%files devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt6/bindings/QtWebEngineCore
%{py3_sitedir}/PyQt6/bindings/QtWebEngineQuick
%{py3_sitedir}/PyQt6/bindings/QtWebEngineWidgets
