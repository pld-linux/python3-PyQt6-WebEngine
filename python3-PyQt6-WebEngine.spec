
%define		module	PyQt6-WebEngine
# minimal required sip version
%define		sip_ver	6.4
# last qt version covered by these bindings (minimal required is currently 5.0.0)
%define		qt_ver	%{version}

Summary:	Python bindings for the Qt6WebEngine module
Summary(pl.UTF-8):	Wiązania Pythona do modułu Qt6WebEngine
Name:		python3-%{module}
Version:	6.4.0
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/P/PyQt6-WebEngine/PyQt6_WebEngine-%{version}.tar.gz
# Source0-md5:	c11453f20b971d5016c4e05d85ed6c4e
URL:		http://www.riverbankcomputing.com/software/pyqtwebengine/
BuildRequires:	Qt6WebEngine-devel >= %{qt_ver}
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt6
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sip-PyQt6 >= 5.15.7
BuildRequires:	sip6 >= %{sip_ver}
Requires:	python3-libs
Obsoletes:	python-PyQtWebEngine < 5.15.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the Qt6WebEngine module.

%description -l pl.UTF-8
Wiązania Pythona do modułu Qt6WebEngine.

%package -n sip-PyQt6-WebEngine
Summary:	SIP files needed to build bindings for Qt6WebEngine
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania wiązań do Qt6WebEngine
Group:		Development/Languages/Python
Requires:	python3-PyQt6-sip >= 13.4.0
Requires:	sip6 >= %{sip_ver}

%description -n sip-PyQt6-WebEngine
SIP files needed to build bindings for Qt6WebEngine.

%description -n sip-PyQt6-WebEngine -l pl.UTF-8
Pliki SIP potrzebne do budowania wiązań do Qt6WebEngine.

%prep
%setup -q -n PyQt6_WebEngine-%{version}

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
%{py3_sitedir}/PyQt6_WebEngine-%{version}.dist-info

%files -n sip-PyQt6-WebEngine
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt6/bindings/QtWebEngineCore
%{py3_sitedir}/PyQt6/bindings/QtWebEngineQuick
%{py3_sitedir}/PyQt6/bindings/QtWebEngineWidgets
