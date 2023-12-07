%define major 6
%define libname %mklibname KSaneWidgets6
%define devname %mklibname KSaneWidgets6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A library for dealing with scanners
Name:		plasma6-libksane
Version:	24.01.80
Release:	1
Group:		System/Libraries
License:	GPLv2
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libksane-%{version}.tar.xz
BuildRequires:	sane-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KSaneCore)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)

%description
LibKSane is a KDE interface for SANE library to control flat scanner.

%files -f libksane.lang
%{_datadir}/icons/*/*/*/*

#------------------------------------------------

%package -n %{libname}
Summary:	A library for dealing with scanners
Group:		System/Libraries
Provides:	ksane = %{EVRD}
Requires:	%{name} = %{EVRD}

%description -n %{libname}
LibKSane is a KDE interface for SANE library to control flat scanners.

%files -n %{libname}
%{_libdir}/libKSaneWidgets6.so.%{major}*
%{_libdir}/libKSaneWidgets6.so.%(echo %{version} |cut -d. -f1)*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	sane-devel
Requires:	%{libname} = %{EVRD}

%description  -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files  -n %{devname}
%{_includedir}/KSaneWidgets6
%{_libdir}/cmake/KSaneWidgets6
%{_libdir}/*.so

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n libksane-%{version}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libksane
