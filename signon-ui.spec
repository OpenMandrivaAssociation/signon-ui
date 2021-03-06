# signon-ui doesn't seem to make releases except
# in the form of ubuntu packages
%define snapshot 20200616
%define debug_package %{nil}

Name:		signon-ui
Version:	0.17
Release:	0.%{snapshot}.2
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
License:	LGPLv2
URL:		http://gitlab.com/accounts-sso/signon-ui
# git clone https://gitlab.com/accounts-sso/signon-ui.git
# git archive --format=tar --prefix signon-ui-0.17/ HEAD | xz -9 > signon-ui-0.17-$(date +%Y%m%d).tar.xz
Source0:	signon-ui-%{version}-%{snapshot}.tar.xz
Patch0:		https://git.archlinux.org/svntogit/packages.git/plain/trunk/fake-user-agent.patch
BuildRequires:	qt5-devel
BuildRequires:	qt5-qttools
BuildRequires:	qt5-qttools-qtdbus
BuildRequires:	qt5-assistant
BuildRequires:	qt5-designer
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	qtchooser
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(signon-plugins)
BuildRequires:	pkgconfig(signon-plugins-common)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(accounts-qt5)
BuildRequires:	pkgconfig(libsignon-qt5)
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
%setup -q
%autopatch -p1
%qmake_qt5 CONFIG+=debug_and_release LIBDIR=%{_libdir} PREFIX=%{_prefix}

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*
%{_datadir}/applications/*.desktop
