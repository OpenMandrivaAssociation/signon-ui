# signon-ui doesn't seem to make releases except
# in the form of ubuntu packages
%define snapshot 20240225
%define debug_package %{nil}

Name:		signon-ui
Version:	0.17
Release:	0.%{snapshot}.1
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
License:	LGPLv2
URL:		http://gitlab.com/accounts-sso/signon-ui
# git clone https://gitlab.com/accounts-sso/signon-ui.git
# git archive --format=tar --prefix signon-ui-0.17/ HEAD | xz -9 > signon-ui-0.17-$(date +%Y%m%d).tar.xz
Source0:	https://gitlab.com/accounts-sso/signon-ui/-/archive/master/signon-ui-master.tar.bz2#/signon-ui-%{snapshot}.tar.bz2
Patch0:		https://git.archlinux.org/svntogit/packages.git/plain/trunk/fake-user-agent.patch
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qttools
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(signon-plugins)
BuildRequires:	pkgconfig(signon-plugins-common)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(accounts-qt6)
BuildRequires:	pkgconfig(libsignon-qt6)
%rename	%{name}
Requires:	dbus
Suggests:	signond

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%prep
%autosetup -p1 -n %{name}-master
%{_qtdir}/bin/qmake CONFIG+=debug_and_release LIBDIR=%{_libdir} PREFIX=%{_prefix}

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*
%{_datadir}/applications/*.desktop
