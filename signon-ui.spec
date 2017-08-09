# signon-ui doesn't seem to make releases except
# in the form of ubuntu packages
%define snapshot 20170809
%define debug_package %{nil}

Name:		signon-ui
Version:	0.17
Release:	0.%{snapshot}.1
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
License:	LGPLv2
URL:		http://gitlab.com/accounts-sso/
# https://gitlab.com/accounts-sso/signon-ui.git
Source0:	signon-ui-%{version}-%{snapshot}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	qt5-qttools
BuildRequires:  qt5-qttools-qtdbus
BuildRequires:  qt5-assistant
BuildRequires:  qt5-designer
BuildRequires:  qt5-linguist
BuildRequires:  qt5-linguist-tools
BuildRequires:  cmake(Qt5Test)
BuildRequires:	qtchooser
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(signon-plugins)
BuildRequires:	pkgconfig(signon-plugins-common)
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
%apply_patches
%qmake_qt5 CONFIG+=debug_and_release LIBDIR=%{_libdir} PREFIX=%{_prefix}

%build
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*
