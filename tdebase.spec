%bcond clang 1
%bcond esound 0
%bcond gamin 1
%bcond tsak 1
%bcond tdehwlib 1
%bcond xrandr 1
%bcond xtest 1
%bcond openexr 1
%bcond xscreensaver 1
%bcond libart 1
%bcond libconfig 1
%bcond kbdledsync 1
%bcond tderandrtray 1
%bcond elficon 0
%bcond ssh 1
%bcond xtst 1
%bcond systemd 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 5

%define tde_pkg tdebase

%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		%{tde_version}
Release:		%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Trinity Base Programs
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

License:		GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

Source2:		pamd.kdm-trinity.omv
Source3:		pamd.kdm-trinity-np.omv
Source4:		pamd.kcheckpass-trinity.omv
Source5:		pamd.kscreensaver-trinity.omv

Obsoletes:	trinity-kdebase < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebase = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebase-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebase-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase = %{?epoch:%{epoch}:}%{version}-%{release}

BuildSystem:  cmake

BuildOption:  -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:  -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:  -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:  -DINCLUDE_INSTALL_DIR="%{tde_prefix}/include/tde"
BuildOption:  -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:  -DXDG_MENU_INSTALL_DIR="%{_sysconfdir}/xdg/menus"
BuildOption:  -DWITH_ALL_OPTIONS=ON -DWITH_SASL=ON -DWITH_LDAP=ON
BuildOption:  -DWITH_SAMBA=ON -DWITH_XCOMPOSITE=ON -DWITH_XCURSOR=ON
BuildOption:  -DWITH_XFIXES=ON -DWITH_XRENDER=ON -DWITH_PCRE=ON
BuildOption:  -DWITH_OPENGL=ON -DWITH_LIBUSB=ON -DWITH_LIBRAW1394=ON
BuildOption:  -DWITH_SUDO_TDESU_BACKEND=ON
BuildOption:  -DWITH_SUDO_KONSOLE_SUPER_USER_COMMAND=ON
BuildOption:  -DWITH_PAM=ON -DWITH_SHADOW=OFF -DWITH_XDMCP=ON
BuildOption:  -DWITH_XINERAMA=ON -DWITH_ARTS=ON -DWITH_I8K=ON
BuildOption:  -DWITH_SENSORS=ON -DWITH_UPOWER=ON
BuildOption:  -DBUILD_ALL=ON 
BuildOption:  -DKCHECKPASS_PAM_SERVICE="kcheckpass-trinity"
BuildOption:  -DTDM_PAM_SERVICE="tdm-trinity"
BuildOption:  -DTDESCREENSAVER_PAM_SERVICE="tdescreensaver-trinity"
BuildOption:  -DHTDIG_SEARCH_BINARY="%{_bindir}/hldig"
BuildOption:  -DBUILD_TDM_SYSTEMD_UNIT_FILE="ON"
BuildOption:  -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:  -DWITH_OPENEXR=%{?!with_openexr:OFF}%{?with_openexr:ON}
BuildOption:  -DWITH_XRANDR=%{?!with_xrandr:OFF}%{?with_xrandr:ON}
BuildOption:  -DWITH_LIBCONFIG=%{?!with_libconfig:OFF}%{?with_libconfig:ON}
BuildOption:  -DWITH_XTEST=%{?!with_xtest:OFF}%{?with_xtest:ON}
BuildOption:  -DWITH_XSCREENSAVER=%{?!with_xscreensaver:OFF}%{?with_xscreensaver:ON}
BuildOption:  -DWITH_LIBART=%{?!with_libart:OFF}%{?with_libart:ON}
BuildOption:  -DWITH_ELFICON=%{!?with_elficon:OFF}%{?with_elficon:ON}
BuildOption:  -DWITH_TDEHWLIB=%{?!with_tdehwlib:OFF}%{?with_tdehwlib:ON}
BuildOption:  -DBUILD_TDEKBDLEDSYNC=%{!?with_kbdledsync:OFF}%{?with_kbdledsync:ON}
BuildOption:  -DBUILD_TSAK=%{!?with_tsak:OFF}%{?with_tsak:ON}

# OpenMandriva
Requires:	distro-release-theme
%define tde_bg /usr/share/wallpapers/default.png

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes

# HTDIG support
BuildRequires:	htdig

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# AUDIOFILE support
BuildRequires:	audiofile-devel

# ALSA supportl
BuildRequires:  pkgconfig(alsa)

# RAW1394 support
BuildRequires:  pkgconfig(libraw1394)

# VORBIS support
BuildRequires:  pkgconfig(vorbis)

# GLIB2 support
BuildRequires:	pkgconfig(glib-2.0)

# PCRE support
BuildRequires:	pkgconfig(libpcreposix)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# SASL support
BuildRequires:  pkgconfig(libsasl2)

# PAM support
BuildRequires:	pkgconfig(pam)

# LIBUSB support
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libusb)

# ESOUND support
%{?with_esound:BuildRequires:	pkgconfig(esound)}

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENLDAP support
BuildRequires:  pkgconfig(ldap)

# SENSORS support
BuildRequires:	lm_sensors-devel

# TSAK support (requires libudev-devel)
#  On RHEL5, udev is built statically, so TSAK cannot build.
BuildRequires:	pkgconfig(udev)

# ACL support
BuildRequires:  pkgconfig(libacl)

# XINERAMA support
BuildRequires:  pkgconfig(xinerama)

# XCOMPOSITE support
BuildRequires:  pkgconfig(xcomposite)

# XCURSOR support
BuildRequires:  pkgconfig(xcursor)

# XRANDR support
%{?with_xrandr:BuildRequires:  pkgconfig(xrandr)}

# XRENDER support
BuildRequires:  pkgconfig(xrender)

BuildRequires:	pkgconfig(xft)

# OPENEXR support
%{?with_openexr:BuildRequires:  pkgconfig(OpenEXR)}

%if %{with xscreensaver}
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  xscreensaver
BuildRequires:  xscreensaver-base
%endif

# AVAHI support
BuildRequires:	libavahi-tqt-devel

# MESA support
BuildRequires:  pkgconfig(glu)

# DBUS support
BuildRequires:	libdbus-tqt-1-devel >= %{tde_epoch}:0.63
BuildRequires:	libdbus-1-tqt-devel >= %{tde_epoch}:0.9
Requires:		libdbus-tqt-1-0 >= %{tde_epoch}:0.63

# LIBART_LGPL support
%{?with_libart:BuildRequires:	pkgconfig(libart-2.0)}

# SAMBA support
BuildRequires:  pkgconfig(smbclient)

# IMAKE
BuildRequires:	imake

# XKB support
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbfile)

# XDMCP support
BuildRequires:  pkgconfig(xdmcp)

# XTST support
%{?with_xtst:BuildRequires:  pkgconfig(xtst)}

# XDAMAGE support
BuildRequires:  pkgconfig(xdamage)

# Requires 'usb.ids'
BuildRequires:	usbutils

# LIBFONTENC support
BuildRequires:  pkgconfig(fontenc)

# Other X11 stuff ...
BuildRequires:	x11-font-util
BuildRequires:	x11-proto-devel

# LIBCONFIG support
# Needed for "compton" stuff
%{?with_libconfig:BuildRequires:  pkgconfig(libconfig)}

# ELFICON support
%{?with_elficon:BuildRequires:		libr-devel >= 0.6.0}

# RPC support
BuildRequires:		pkgconfig(libtirpc)
BuildRequires:    pkgconfig(libnsl)

# ATTR support
BuildRequires: pkgconfig(libattr)

# LIBSSH support
%{?with_ssh:BuildRequires:	libssh-devel}

# tdebase is a metapackage that installs all sub-packages
Requires: %{name}-runtime-data-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-pim-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kappfinder = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kate = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kwrite = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kcontrol = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdepasswd = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdeprint = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdm = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kfind = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-khelpcenter = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kicker = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klipper = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmenuedit = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konqueror = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konqueror-nsplugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konsole = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpager = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpersonalizer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksmserver = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksplash = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksysguard = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksysguardd = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktip = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-twin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-libtqt3-integration = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-smb-plugin = %{?epoch:%{epoch}:}%{version}-%{release}
 
Requires:	trinity-arts >= %{tde_epoch}:1.5.10
Requires:	trinity-tdelibs >= %{tde_version}

%description
TDE (the Trinity Desktop Environment) is a powerful Open Source graphical
desktop environment for Unix workstations. It combines ease of use,
contemporary functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This metapackage includes the nucleus of TDE, namely the minimal package
set necessary to run TDE as a desktop environment. This includes the
window manager, taskbar, control center, a text editor, file manager,
web browser, X terminal emulator, and many other programs and components.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS README README.pam
%{tde_prefix}/bin/tde_release_notes
%{tde_prefix}/share/autostart/tde_release_notes.desktop
%{tde_prefix}/share/applications/tde/tdehtml_userinterface.desktop

##########

%package devel
Summary:	%{summary} - Development files
Group:		Development/Libraries/Other
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
Requires:	trinity-tdelibs-devel >= %{tde_version}

Requires:	%{name}-bin-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kate-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kcontrol-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kdesktop-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kicker-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-konqueror-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ksplash-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ksysguard-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkonq-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdm-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-twin-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Provides:	trinity-kdebase-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This is a meta-package that installs all tdebase development packages.

Header files for developing applications using %{name}.
Install tdebase-devel if you want to develop or compile Konqueror,
Kate plugins or TWin styles.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/share/cmake/*.cmake

##########

%package tdeio-pim-plugins
Summary:	PIM TDEIOslaves from %{name}
Group:		System/GUI/Other

Provides:	trinity-kdebase-pim-ioslaves = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-pim-ioslaves < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-kio-pim-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-kio-pim-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdebase-kio-pim-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdebase-kio-pim-plugins < %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-pim-plugins
Protocol handlers (TDEIOslaves) for personal information management, including:
 * tdeio_ldap
 * tdeio_nntp
 * tdeio_pop3
 * tdeio_smtp

%files tdeio-pim-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdeio_ldap.la
%{tde_prefix}/%{_lib}/trinity/tdeio_ldap.so
%{tde_prefix}/%{_lib}/trinity/tdeio_nntp.la
%{tde_prefix}/%{_lib}/trinity/tdeio_nntp.so
%{tde_prefix}/%{_lib}/trinity/tdeio_pop3.la
%{tde_prefix}/%{_lib}/trinity/tdeio_pop3.so
%{tde_prefix}/%{_lib}/trinity/tdeio_smtp.la
%{tde_prefix}/%{_lib}/trinity/tdeio_smtp.so
%{tde_prefix}/share/services/ldap.protocol
%{tde_prefix}/share/services/ldaps.protocol
%{tde_prefix}/share/services/nntp.protocol
%{tde_prefix}/share/services/nntps.protocol
%{tde_prefix}/share/services/pop3.protocol
%{tde_prefix}/share/services/pop3s.protocol
%{tde_prefix}/share/services/smtp.protocol
%{tde_prefix}/share/services/smtps.protocol

##########

%package runtime-data-common
Summary:	Shared common files for Trinity and KDE4
Group:		System/GUI/Other

Provides:	tdebase-runtime-data-common = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-runtime-data-common < %{?epoch:%{epoch}:}%{version}-%{release}

%description runtime-data-common
Shared common files for both Trinity and KDE4
Such as the desktop right-click-"Create New" list

%files runtime-data-common
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kxkb/
%{tde_prefix}/share/desktop-directories/
%{tde_prefix}/share/icons/hicolor/*/apps/kxkb.png
%{tde_prefix}/share/icons/hicolor/*/apps/knetattach.*
%{tde_prefix}/share/icons/hicolor/*/apps/khotkeys.png
%{tde_prefix}/share/icons/hicolor/*/apps/kmenuedit.png
%{tde_prefix}/share/icons/hicolor/*/apps/ksplash.png
%{tde_prefix}/share/locale/en_US/entry.desktop
%{tde_prefix}/share/locale/l10n/*.desktop
%{tde_prefix}/share/locale/l10n/*/entry.desktop
%{tde_prefix}/share/locale/l10n/*/flag.png
%{tde_prefix}/share/sounds/pop.wav
%{tde_prefix}/share/templates/

##########

%package -n trinity-kappfinder
Summary:	Non-TDE application finder for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kappfinder
kappfinder searches your workstation for many common applications and
creates menu entries for them.

%files -n trinity-kappfinder
%defattr(-,root,root,-)
%{tde_prefix}/bin/kappfinder
%{tde_prefix}/share/applications/tde/kappfinder.desktop
%{tde_prefix}/share/applnk/System/kappfinder.desktop
%{tde_prefix}/share/apps/kappfinder
%{tde_prefix}/share/icons/hicolor/*/apps/kappfinder.png
%{tde_prefix}/share/man/man1/kappfinder.1*

##########

%package -n trinity-libkateinterfaces
Summary:	Common libraries used by kwrite and kate
Group:		System/GUI/Other

%description -n trinity-libkateinterfaces
This package contains the kateinterface library.

%files -n trinity-libkateinterfaces
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkateinterfaces.so.*

##########

%package -n trinity-kate
Summary:	Advanced text editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kwrite = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkateinterfaces = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kate
Kate is a multi document editor, based on a rewritten version of the kwrite
editing widget of TDE.

It is a multi-view editor that lets you view several instances of the same
document with all instances being synced, or view more files at the same
time for easy reference or simultaneous editing. The terminal emulation
and sidebar are docked windows that can be plugged out of the main window,
or replaced therein according to your preference.

Some random features:
* Editing of big files
* Extensible syntax highlighting
* Folding
* Dynamic word wrap
* Selectable encoding
* Filter command
* Global grep dialog

%files -n trinity-kate
%defattr(-,root,root,-)
%{tde_prefix}/bin/kate
%{tde_prefix}/%{_lib}/trinity/kate.la
%{tde_prefix}/%{_lib}/trinity/kate.so
%{tde_prefix}/%{_lib}/libkateutils.so.*
%{tde_prefix}/%{_lib}/libtdeinit_kate.la
%{tde_prefix}/%{_lib}/libtdeinit_kate.so
%{tde_prefix}/share/applications/tde/kate.desktop
%{tde_prefix}/share/apps/kate/
%{tde_prefix}/share/apps/tdeconf_update/kate-2.4.upd
%config(noreplace) %{_sysconfdir}/trinity/katerc
%{tde_prefix}/share/icons/hicolor/*/apps/kate.png
%{tde_prefix}/share/icons/hicolor/*/apps/kate2.svgz
%{tde_prefix}/share/servicetypes/kateplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kate/
%{tde_prefix}/share/man/man1/kate.1*

##########

%package -n trinity-kate-devel
Summary:	Development files for kate
Group:		Development/Libraries/Other
Requires:	trinity-kate = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kate-devel
This package contains the development files fare Kate.

%files -n trinity-kate-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kate/
%{tde_prefix}/%{_lib}/libkateutils.so
%{tde_prefix}/%{_lib}/libkateutils.la
%{tde_prefix}/%{_lib}/libkateinterfaces.so
%{tde_prefix}/%{_lib}/libkateinterfaces.la

##########

%package -n trinity-kwrite
Summary:	Advanced text editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkateinterfaces = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kwrite
Kwrite is an advanced text editor for TDE.

%files -n trinity-kwrite
%defattr(-,root,root,-)
%{tde_prefix}/bin/kwrite
%{tde_prefix}/%{_lib}/trinity/kwrite.la
%{tde_prefix}/%{_lib}/trinity/kwrite.so
%{tde_prefix}/%{_lib}/libtdeinit_kwrite.la
%{tde_prefix}/%{_lib}/libtdeinit_kwrite.so
%{tde_prefix}/share/applications/tde/kwrite.desktop
%{tde_prefix}/share/apps/kwrite/
%{tde_prefix}/share/icons/hicolor/*/apps/kwrite.png
%{tde_prefix}/share/icons/hicolor/*/apps/kwrite2.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kwrite/
%{tde_prefix}/share/man/man1/kwrite.1*

##########

%package -n trinity-kcontrol
Summary:	Control center for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

# Requires 'usb.ids'
Requires:		usbutils
BuildRequires:	usbutils

%description -n trinity-kcontrol
The Trinity Control Center provides you with a centralized and convenient
way to configure all of your TDE settings.

It is made up of multiple modules. Each module is a separate application,
but the control center organizes all of these programs into a convenient
location.

In combination with udev KControl supports the advanced
configuration of Logitech mice, though the user must be a member of the
plugdev group.

%files -n trinity-kcontrol
%defattr(-,root,root,-)
%{tde_prefix}/bin/kaccess
%{tde_prefix}/bin/kcontrol
%{tde_prefix}/bin/kdeinstallktheme
%{tde_prefix}/bin/keditfiletype
%{tde_prefix}/bin/tdefontinst
%{tde_prefix}/bin/tdefontview
%{tde_prefix}/bin/klocaldomainurifilterhelper
%{tde_prefix}/bin/krdb
%{tde_prefix}/%{_lib}/trinity/fontthumbnail.la
%{tde_prefix}/%{_lib}/trinity/fontthumbnail.so
%{tde_prefix}/%{_lib}/trinity/kaccess.la
%{tde_prefix}/%{_lib}/trinity/kaccess.so
%{tde_prefix}/%{_lib}/trinity/kcm_access.la
%{tde_prefix}/%{_lib}/trinity/kcm_access.so
%{tde_prefix}/%{_lib}/trinity/kcm_arts.la
%{tde_prefix}/%{_lib}/trinity/kcm_arts.so
%{tde_prefix}/%{_lib}/trinity/kcm_background.la
%{tde_prefix}/%{_lib}/trinity/kcm_background.so
%{tde_prefix}/%{_lib}/trinity/kcm_bell.la
%{tde_prefix}/%{_lib}/trinity/kcm_bell.so
%{tde_prefix}/%{_lib}/trinity/kcm_clock.la
%{tde_prefix}/%{_lib}/trinity/kcm_clock.so
%{tde_prefix}/%{_lib}/trinity/kcm_colors.la
%{tde_prefix}/%{_lib}/trinity/kcm_colors.so
%{tde_prefix}/%{_lib}/trinity/kcm_componentchooser.la
%{tde_prefix}/%{_lib}/trinity/kcm_componentchooser.so
%{tde_prefix}/%{_lib}/trinity/kcm_crypto.la
%{tde_prefix}/%{_lib}/trinity/kcm_crypto.so
%{tde_prefix}/%{_lib}/trinity/kcm_css.la
%{tde_prefix}/%{_lib}/trinity/kcm_css.so
%{tde_prefix}/%{_lib}/trinity/kcm_display.la
%{tde_prefix}/%{_lib}/trinity/kcm_display.so
%{tde_prefix}/%{_lib}/trinity/kcm_energy.la
%{tde_prefix}/%{_lib}/trinity/kcm_energy.so
%{tde_prefix}/%{_lib}/trinity/kcm_filetypes.la
%{tde_prefix}/%{_lib}/trinity/kcm_filetypes.so
%{tde_prefix}/%{_lib}/trinity/kcm_fontinst.la
%{tde_prefix}/%{_lib}/trinity/kcm_fontinst.so
%{tde_prefix}/%{_lib}/trinity/kcm_fonts.la
%{tde_prefix}/%{_lib}/trinity/kcm_fonts.so
%if %{with tdehwlib}
%{tde_prefix}/%{_lib}/trinity/kcm_hwmanager.la
%{tde_prefix}/%{_lib}/trinity/kcm_hwmanager.so
%endif
%{tde_prefix}/%{_lib}/trinity/kcm_icons.la
%{tde_prefix}/%{_lib}/trinity/kcm_icons.so
%{tde_prefix}/%{_lib}/trinity/kcm_info.la
%{tde_prefix}/%{_lib}/trinity/kcm_info.so
%{tde_prefix}/%{_lib}/trinity/kcm_input.la
%{tde_prefix}/%{_lib}/trinity/kcm_input.so
%{tde_prefix}/%{_lib}/trinity/kcm_joystick.la
%{tde_prefix}/%{_lib}/trinity/kcm_joystick.so
%{tde_prefix}/%{_lib}/trinity/kcm_kded.la
%{tde_prefix}/%{_lib}/trinity/kcm_kded.so
%{tde_prefix}/%{_lib}/trinity/kcm_tdm.la
%{tde_prefix}/%{_lib}/trinity/kcm_tdm.so
%{tde_prefix}/%{_lib}/trinity/kcm_tdednssd.so
%{tde_prefix}/%{_lib}/trinity/kcm_tdednssd.la
%{tde_prefix}/%{_lib}/trinity/kcm_keys.la
%{tde_prefix}/%{_lib}/trinity/kcm_keys.so
%{tde_prefix}/%{_lib}/trinity/kcm_kicker.la
%{tde_prefix}/%{_lib}/trinity/kcm_kicker.so
%{tde_prefix}/%{_lib}/trinity/kcm_tdeio.la
%{tde_prefix}/%{_lib}/trinity/kcm_tdeio.so
%{tde_prefix}/%{_lib}/trinity/kcm_knotify.la
%{tde_prefix}/%{_lib}/trinity/kcm_knotify.so
%{tde_prefix}/%{_lib}/trinity/kcm_konqhtml.la
%{tde_prefix}/%{_lib}/trinity/kcm_konqhtml.so
%{tde_prefix}/%{_lib}/trinity/kcm_konq.la
%{tde_prefix}/%{_lib}/trinity/kcm_konq.so
%{tde_prefix}/%{_lib}/trinity/kcm_kthememanager.la
%{tde_prefix}/%{_lib}/trinity/kcm_kthememanager.so
%{tde_prefix}/%{_lib}/trinity/kcm_kurifilt.la
%{tde_prefix}/%{_lib}/trinity/kcm_kurifilt.so
%{tde_prefix}/%{_lib}/trinity/kcm_launch.la
%{tde_prefix}/%{_lib}/trinity/kcm_launch.so
%{tde_prefix}/%{_lib}/trinity/kcm_locale.la
%{tde_prefix}/%{_lib}/trinity/kcm_locale.so
%{tde_prefix}/%{_lib}/trinity/kcm_nic.la
%{tde_prefix}/%{_lib}/trinity/kcm_nic.so
%{tde_prefix}/%{_lib}/trinity/kcm_performance.la
%{tde_prefix}/%{_lib}/trinity/kcm_performance.so
%{tde_prefix}/%{_lib}/trinity/kcm_privacy.la
%{tde_prefix}/%{_lib}/trinity/kcm_privacy.so
%{tde_prefix}/%{_lib}/trinity/kcm_screensaver.la
%{tde_prefix}/%{_lib}/trinity/kcm_screensaver.so
%{tde_prefix}/%{_lib}/trinity/kcm_smserver.la
%{tde_prefix}/%{_lib}/trinity/kcm_smserver.so
%{tde_prefix}/%{_lib}/trinity/kcm_spellchecking.la
%{tde_prefix}/%{_lib}/trinity/kcm_spellchecking.so
%{tde_prefix}/%{_lib}/trinity/kcm_style.la
%{tde_prefix}/%{_lib}/trinity/kcm_style.so
%{tde_prefix}/%{_lib}/trinity/kcm_taskbar.la
%{tde_prefix}/%{_lib}/trinity/kcm_taskbar.so
%{tde_prefix}/%{_lib}/trinity/kcm_usb.la
%{tde_prefix}/%{_lib}/trinity/kcm_usb.so
%{tde_prefix}/%{_lib}/trinity/kcm_view1394.la
%{tde_prefix}/%{_lib}/trinity/kcm_view1394.so
%{tde_prefix}/%{_lib}/trinity/kcm_xinerama.la
%{tde_prefix}/%{_lib}/trinity/kcm_xinerama.so
%{tde_prefix}/%{_lib}/trinity/kcontrol.la
%{tde_prefix}/%{_lib}/trinity/kcontrol.so
%{tde_prefix}/%{_lib}/trinity/tdefile_font.la
%{tde_prefix}/%{_lib}/trinity/tdefile_font.so
%{tde_prefix}/%{_lib}/trinity/tdeio_fonts.la
%{tde_prefix}/%{_lib}/trinity/tdeio_fonts.so
%{tde_prefix}/%{_lib}/trinity/tdestyle_keramik_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_keramik_config.so
%{tde_prefix}/%{_lib}/trinity/libtdefontviewpart.la
%{tde_prefix}/%{_lib}/trinity/libtdefontviewpart.so
%{tde_prefix}/%{_lib}/trinity/libtdeshorturifilter.la
%{tde_prefix}/%{_lib}/trinity/libtdeshorturifilter.so
%{tde_prefix}/%{_lib}/trinity/libkuriikwsfilter.la
%{tde_prefix}/%{_lib}/trinity/libkuriikwsfilter.so
%{tde_prefix}/%{_lib}/trinity/libkurisearchfilter.la
%{tde_prefix}/%{_lib}/trinity/libkurisearchfilter.so
%{tde_prefix}/%{_lib}/trinity/liblocaldomainurifilter.la
%{tde_prefix}/%{_lib}/trinity/liblocaldomainurifilter.so
%{tde_prefix}/%{_lib}/libtdeinit_kaccess.la
%{tde_prefix}/%{_lib}/libtdeinit_kaccess.so
%{tde_prefix}/%{_lib}/libtdeinit_kcontrol.la
%{tde_prefix}/%{_lib}/libtdeinit_kcontrol.so
%{tde_prefix}/%{_lib}/libtdefontinst.so.*
%{tde_prefix}/share/applications/tde/arts.desktop
%{tde_prefix}/share/applications/tde/background.desktop
%{tde_prefix}/share/applications/tde/bell.desktop
%{tde_prefix}/share/applications/tde/cache.desktop
%{tde_prefix}/share/applications/tde/cdinfo.desktop
%{tde_prefix}/share/applications/tde/clock.desktop
%{tde_prefix}/share/applications/tde/colors.desktop
%{tde_prefix}/share/applications/tde/componentchooser.desktop
%{tde_prefix}/share/applications/tde/cookies.desktop
%{tde_prefix}/share/applications/tde/crypto.desktop
%{tde_prefix}/share/applications/tde/desktopbehavior.desktop
%{tde_prefix}/share/applications/tde/desktop.desktop
%{tde_prefix}/share/applications/tde/desktoppath.desktop
%{tde_prefix}/share/applications/tde/devices.desktop
%{tde_prefix}/share/applications/tde/display.desktop
%{tde_prefix}/share/applications/tde/dma.desktop
%{tde_prefix}/share/applications/tde/ebrowsing.desktop
%{tde_prefix}/share/applications/tde/filebrowser.desktop
%{tde_prefix}/share/applications/tde/filetypes.desktop
%{tde_prefix}/share/applications/tde/fonts.desktop
%{?with_tdehwlib:%{tde_prefix}/share/applications/tde/hwmanager.desktop}
%{tde_prefix}/share/applications/tde/icons.desktop
%{tde_prefix}/share/applications/tde/installktheme.desktop
%{tde_prefix}/share/applications/tde/interrupts.desktop
%{tde_prefix}/share/applications/tde/ioports.desktop
%{tde_prefix}/share/applications/tde/joystick.desktop
%{tde_prefix}/share/applications/tde/kcm_tdednssd.desktop
%{tde_prefix}/share/applications/tde/kcmaccess.desktop
%{tde_prefix}/share/applications/tde/kcmcss.desktop
%{tde_prefix}/share/applications/tde/kcmfontinst.desktop
%{tde_prefix}/share/applications/tde/kcmkded.desktop
%{tde_prefix}/share/applications/tde/kcmlaunch.desktop
%{tde_prefix}/share/applications/tde/kcmnotify.desktop
%{tde_prefix}/share/applications/tde/kcmperformance.desktop
%{tde_prefix}/share/applications/tde/kcmsmserver.desktop
%{tde_prefix}/share/applications/tde/kcmtaskbar.desktop
%{tde_prefix}/share/applications/tde/kcmusb.desktop
%{tde_prefix}/share/applications/tde/kcmview1394.desktop
%{tde_prefix}/share/applications/tde/KControl.desktop
%{tde_prefix}/share/applications/tde/tdm.desktop
%{tde_prefix}/share/applications/tde/keys.desktop
%{tde_prefix}/share/applications/tde/tdefontview.desktop
%{tde_prefix}/share/applications/tde/tdehtml_behavior.desktop
%{tde_prefix}/share/applications/tde/tdehtml_fonts.desktop
%{tde_prefix}/share/applications/tde/tdehtml_java_js.desktop
%{tde_prefix}/share/applications/tde/kthememanager.desktop
%{tde_prefix}/share/applications/tde/lanbrowser.desktop
%{tde_prefix}/share/applications/tde/language.desktop
%{tde_prefix}/share/applications/tde/media.desktop
%{tde_prefix}/share/applications/tde/memory.desktop
%{tde_prefix}/share/applications/tde/mouse.desktop
%{tde_prefix}/share/applications/tde/netpref.desktop
%{tde_prefix}/share/applications/tde/nic.desktop
%{tde_prefix}/share/applications/tde/opengl.desktop
%{tde_prefix}/share/applications/tde/panel_appearance.desktop
%{tde_prefix}/share/applications/tde/panel.desktop
%{tde_prefix}/share/applications/tde/partitions.desktop
%{tde_prefix}/share/applications/tde/pci.desktop
%{tde_prefix}/share/applications/tde/privacy.desktop
%{tde_prefix}/share/applications/tde/processor.desktop
%{tde_prefix}/share/applications/tde/proxy.desktop
%{tde_prefix}/share/applications/tde/screensaver.desktop
%{tde_prefix}/share/applications/tde/scsi.desktop
%{tde_prefix}/share/applications/tde/smbstatus.desktop
%{tde_prefix}/share/applications/tde/sound.desktop
%{tde_prefix}/share/applications/tde/spellchecking.desktop
%{tde_prefix}/share/applications/tde/style.desktop
%{tde_prefix}/share/applications/tde/tde-kcontrol.desktop
%{tde_prefix}/share/applications/tde/useragent.desktop
%{tde_prefix}/share/applications/tde/xserver.desktop
%{tde_prefix}/share/applnk/.hidden/energy.desktop
%{tde_prefix}/share/applnk/.hidden/fileappearance.desktop
%{tde_prefix}/share/applnk/.hidden/filebehavior.desktop
%{tde_prefix}/share/applnk/.hidden/filepreviews.desktop
%{tde_prefix}/share/applnk/.hidden/kcmkonqyperformance.desktop
%{tde_prefix}/share/applnk/.hidden/kicker_config_appearance.desktop
%{tde_prefix}/share/applnk/.hidden/kicker_config.desktop
%{tde_prefix}/share/applnk/.hidden/smb.desktop
%{tde_prefix}/share/applnk/.hidden/xinerama.desktop
%{tde_prefix}/share/applnk/Settings/LookNFeel/
%{tde_prefix}/share/applnk/Settings/WebBrowsing/tdehtml_appearance.desktop
%{tde_prefix}/share/applnk/Settings/WebBrowsing/nsplugin.desktop
%{tde_prefix}/share/applnk/Settings/WebBrowsing/smb.desktop
%{tde_prefix}/share/apps/kcm_componentchooser/kcm_browser.desktop
%{tde_prefix}/share/apps/kcm_componentchooser/kcm_kemail.desktop
%{tde_prefix}/share/apps/kcm_componentchooser/kcm_filemanager.desktop
%{tde_prefix}/share/apps/kcm_componentchooser/kcm_terminal.desktop
%{tde_prefix}/share/apps/kcmview1394/
%{tde_prefix}/share/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/installfont.desktop
%{tde_prefix}/share/apps/usb.ids
%{tde_prefix}/share/mimelnk/application/x-ktheme.desktop
%{tde_prefix}/share/mimelnk/fonts/folder.desktop
%{tde_prefix}/share/mimelnk/fonts/package.desktop
%{tde_prefix}/share/mimelnk/fonts/system-folder.desktop
%{tde_prefix}/share/services/fonts.protocol
%{tde_prefix}/share/services/fontthumbnail.desktop
%{tde_prefix}/share/services/kaccess.desktop
%{tde_prefix}/share/services/tdefile_font.desktop
%{tde_prefix}/share/services/tdefontviewpart.desktop
%{tde_prefix}/share/services/tdeshorturifilter.desktop
%{tde_prefix}/share/services/kuriikwsfilter.desktop
%{tde_prefix}/share/services/kurisearchfilter.desktop
%{tde_prefix}/share/services/localdomainurifilter.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kcmcolors.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmcomponentchooser.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmdesktop.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmdesktopbehavior.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmkdnssd.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmlaunch.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmmedia.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmmouse.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmnetpref.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmnic.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmperformance.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmprivacy.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmtaskbar.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmcgi.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmcrypto.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmhistory.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmjoystick.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmkded.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmkhtml_filter.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmsmserver.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmspellchecking.png
%{tde_prefix}/share/doc/tde/HTML/en/tdefontview/

# tdehwtray
%{tde_prefix}/bin/tdehwdevicetray
%{tde_prefix}/share/applications/tde/tdehwdevicetray.desktop
%{tde_prefix}/share/autostart/tdehwdevicetray-autostart.desktop

# tdesyndaemon
%{tde_prefix}/bin/tdesyndaemon
%{tde_prefix}/share/applications/tde/touchpad.desktop
%{tde_prefix}/share/apps/tdeconf_update/remote_folder_icon.upd
%{tde_prefix}/share/apps/tdeconf_update/remote_folder_icon_upd.sh
%{tde_prefix}/share/icons/crystalsvg/*/devices/input-touchpad.png
%{tde_prefix}/share/icons/crystalsvg/scalable/devices/input-touchpad.svg
%{tde_prefix}/share/services/kded/khotkeys.desktop

# The following features are not compiled under RHEL 5 and older
%if %{with tderandrtray}
%{tde_prefix}/bin/tderandrtray
%{tde_prefix}/%{_lib}/trinity/kcm_displayconfig.la
%{tde_prefix}/%{_lib}/trinity/kcm_displayconfig.so
%{tde_prefix}/%{_lib}/trinity/kcm_iccconfig.la
%{tde_prefix}/%{_lib}/trinity/kcm_iccconfig.so
%{tde_prefix}/%{_lib}/trinity/kcm_randr.la
%{tde_prefix}/%{_lib}/trinity/kcm_randr.so
%{tde_prefix}/share/applications/tde/displayconfig.desktop
%{tde_prefix}/share/applications/tde/iccconfig.desktop
%{tde_prefix}/share/applications/tde/tderandrtray.desktop
%{tde_prefix}/share/applnk/.hidden/randr.desktop
%{tde_prefix}/share/autostart/tderandrtray-autostart.desktop
%{tde_prefix}/share/doc/tde/HTML/en/tderandrtray/
%endif

##########

%package -n trinity-kcontrol-devel
Summary:	Development files for kcontrol
Group:		Development/Libraries/Other
Requires:	trinity-kcontrol = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kcontrol-devel
%{summary}.

%files -n trinity-kcontrol-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libtdefontinst.la
%{tde_prefix}/%{_lib}/libtdefontinst.so

##########

%package bin
Summary:	Core binaries for the TDE base module
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	pam

Provides:	tdebase-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-bin < %{?epoch:%{epoch}:}%{version}-%{release}

%description bin
This package contains miscellaneous programs needed by other
TDE applications, particularly those in the TDE base module.

%files bin
%defattr(-,root,root,-)
%{tde_prefix}/bin/krootbacking
%{?with_tsak:%{tde_prefix}/bin/tsak}
%{?with_libconfig:%{tde_prefix}/bin/compton-tde}
%{tde_prefix}/bin/tdedebugdialog
%{tde_prefix}/bin/kreadconfig
%{tde_prefix}/bin/kwriteconfig
%{tde_prefix}/bin/kstart
%config(noreplace) %{_sysconfdir}/trinity/kxkb_groups
%{tde_prefix}/bin/drkonqi
%{tde_prefix}/bin/crashtest
%{tde_prefix}/bin/kapplymousetheme
%{tde_prefix}/bin/kblankscrn.kss
%{tde_prefix}/bin/kcminit
%{tde_prefix}/bin/kcminit_startup
%{tde_prefix}/bin/kdcop
%{tde_prefix}/bin/tdesu
%attr(0755,root,root) %{tde_prefix}/bin/tdesud
%{tde_prefix}/bin/kdialog
%{tde_prefix}/bin/khotkeys
%{tde_prefix}/bin/knetattach
%{tde_prefix}/bin/krandom.kss
%{tde_prefix}/bin/ksystraycmd
%{tde_prefix}/bin/kxkb
%{tde_prefix}/bin/tde_license_info
%{tde_prefix}/bin/tde_show_license_info
%dir %{tde_prefix}/%{_lib}/tdeconf_update_bin
%{tde_prefix}/%{_lib}/tdeconf_update_bin/khotkeys_update
%{tde_prefix}/%{_lib}/trinity/kcminit.la
%{tde_prefix}/%{_lib}/trinity/kcminit.so
%{tde_prefix}/%{_lib}/trinity/kcminit_startup.la
%{tde_prefix}/%{_lib}/trinity/kcminit_startup.so
%{tde_prefix}/%{_lib}/trinity/kcm_keyboard.la
%{tde_prefix}/%{_lib}/trinity/kcm_keyboard.so
%{tde_prefix}/%{_lib}/trinity/kcm_khotkeys.la
%{tde_prefix}/%{_lib}/trinity/kcm_khotkeys.so
%{tde_prefix}/%{_lib}/trinity/kded_khotkeys.la
%{tde_prefix}/%{_lib}/trinity/kded_khotkeys.so
%{tde_prefix}/%{_lib}/trinity/kgreet_classic.la
%{tde_prefix}/%{_lib}/trinity/kgreet_classic.so
%{tde_prefix}/%{_lib}/trinity/kgreet_winbind.la
%{tde_prefix}/%{_lib}/trinity/kgreet_winbind.so
%{tde_prefix}/%{_lib}/trinity/khotkeys.la
%{tde_prefix}/%{_lib}/trinity/khotkeys.so
%{tde_prefix}/%{_lib}/trinity/khotkeys_arts.la
%{tde_prefix}/%{_lib}/trinity/khotkeys_arts.so
%{tde_prefix}/%{_lib}/trinity/kxkb.la
%{tde_prefix}/%{_lib}/trinity/kxkb.so
%{tde_prefix}/%{_lib}/libtdeinit_kcminit.la
%{tde_prefix}/%{_lib}/libtdeinit_kcminit.so
%{tde_prefix}/%{_lib}/libtdeinit_kcminit_startup.la
%{tde_prefix}/%{_lib}/libtdeinit_kcminit_startup.so
%{tde_prefix}/%{_lib}/libtdeinit_khotkeys.la
%{tde_prefix}/%{_lib}/libtdeinit_khotkeys.so
%{tde_prefix}/%{_lib}/libtdeinit_kxkb.la
%{tde_prefix}/%{_lib}/libtdeinit_kxkb.so
%{tde_prefix}/%{_lib}/libkhotkeys_shared.so.*
%{tde_prefix}/share/applications/tde/kdcop.desktop
%{tde_prefix}/share/applications/tde/keyboard.desktop
%{tde_prefix}/share/applications/tde/keyboard_layout.desktop
%{tde_prefix}/share/applications/tde/khotkeys.desktop
%{tde_prefix}/share/applications/tde/knetattach.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/
%{tde_prefix}/share/apps/drkonqi/
%{tde_prefix}/share/apps/tdeconf_update/khotkeys_32b1_update.upd
%{tde_prefix}/share/apps/tdeconf_update/khotkeys_printscreen.upd
%{tde_prefix}/share/apps/tdeconf_update/konqueror_gestures_trinity21_update.upd
%{tde_prefix}/share/apps/kdcop/
%{tde_prefix}/share/apps/khotkeys/
%{tde_prefix}/share/autostart/tde_license_info.desktop
%{tde_prefix}/share/services/kxkb.desktop
%config(noreplace) %{_sysconfdir}/pam.d/kcheckpass-trinity
%config(noreplace) %{_sysconfdir}/pam.d/tdescreensaver-trinity
%{tde_prefix}/share/doc/tde/HTML/en/kdcop/
%{tde_prefix}/share/doc/tde/HTML/en/tdedebugdialog//
%{tde_prefix}/share/doc/tde/HTML/en/tdesu/
%{tde_prefix}/share/doc/tde/HTML/en/knetattach/
%{tde_prefix}/share/doc/tde/HTML/en/kxkb/
%{tde_prefix}/share/man/man1/drkonqi.1*
%{tde_prefix}/share/man/man1/kblankscrn.kss.1*
%{tde_prefix}/share/man/man1/kcheckpass.1*
%{tde_prefix}/share/man/man1/kcminit.1*
%{tde_prefix}/share/man/man1/kdcop.1*
%{tde_prefix}/share/man/man1/kdialog.1*
%{tde_prefix}/share/man/man1/khotkeys.1*
%{tde_prefix}/share/man/man1/knetattach.1*
%{tde_prefix}/share/man/man1/krandom.kss.1*
%{tde_prefix}/share/man/man1/kreadconfig.1*
%{tde_prefix}/share/man/man1/kstart.1*
%{tde_prefix}/share/man/man1/ksystraycmd.1*
%{tde_prefix}/share/man/man1/kwriteconfig.1*
%{tde_prefix}/share/man/man1/kxkb.1*
%{tde_prefix}/share/man/man1/tdedebugdialog.1*
%{tde_prefix}/share/man/man1/tdesu.1*

# SETUID binaries
# Some setuid binaries need special care
%{?with_tsak:%attr(4511,root,root) %{tde_prefix}/bin/tdmtsak}
%attr(4755,root,root) %{tde_prefix}/bin/kcheckpass
%{?with_kbdledsync:%attr(4755,root,root) %{tde_prefix}/bin/tdekbdledsync}

%package bin-devel
Summary:	Development files for core binaries for the TDE base module
Group:		Development/Libraries/Other
Requires:	%{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

Obsoletes:	tdebase-bin-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-bin-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description bin-devel
This package contains the development files for core binaries for 
the TDE base module

%files bin-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkhotkeys_shared.la
%{tde_prefix}/%{_lib}/libkhotkeys_shared.so

##########

%package data
Summary:	Shared data files for the TDE base module
Group:		System/GUI/Other
Requires:	%{name}-runtime-data-common = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	tdebase-data < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description data
This package contains the architecture-independent shared data files
needed for a basic TDE desktop installation.

%files data
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/tdeshorturifilterrc
%{tde_prefix}/share/applnk/.hidden/battery.desktop
%{tde_prefix}/share/applnk/.hidden/bwarning.desktop
%{tde_prefix}/share/applnk/.hidden/cwarning.desktop
%{tde_prefix}/share/applnk/.hidden/.directory
%{tde_prefix}/share/applnk/.hidden/email.desktop
%{tde_prefix}/share/applnk/.hidden/kcmkonq.desktop
%{tde_prefix}/share/applnk/.hidden/kcmkxmlrpcd.desktop
%{tde_prefix}/share/applnk/.hidden/konqhtml.desktop
%{tde_prefix}/share/applnk/.hidden/passwords.desktop
%{tde_prefix}/share/applnk/.hidden/power.desktop
%{tde_prefix}/share/applnk/.hidden/socks.desktop
%{tde_prefix}/share/applnk/.hidden/userinfo.desktop
%{tde_prefix}/share/applnk/.hidden/virtualdesktops.desktop
%{tde_prefix}/share/apps/kaccess/
%{tde_prefix}/share/apps/kcmcss/
%{tde_prefix}/share/apps/kcminput/
%{tde_prefix}/share/apps/kcmkeys/
%{tde_prefix}/share/apps/kcmlocale/
%{tde_prefix}/share/apps/tdeconf_update/convertShortcuts.pl
%{tde_prefix}/share/apps/tdeconf_update/tdeaccel.upd
%{tde_prefix}/share/apps/tdeconf_update/kcmdisplayrc.upd
%{tde_prefix}/share/apps/tdeconf_update/kuriikwsfilter.upd
%{tde_prefix}/share/apps/tdeconf_update/mouse_cursor_theme.upd
%{tde_prefix}/share/apps/tdeconf_update/socks.upd
%{tde_prefix}/share/apps/kcontrol/
%{tde_prefix}/share/apps/tdedisplay/
%{tde_prefix}/share/apps/tdefontview/
%{tde_prefix}/share/apps/kthememanager/
%{tde_prefix}/share/icons/crystalsvg/*/apps/access.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/acroread.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/applixware.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/arts.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/background.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/bell.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/cache.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/clanbomber.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/clock.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/colors.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/date.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/email.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/energy.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/energy_star.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/filetypes.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/fonts.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gimp.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/help_index.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/hwinfo.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmdevices.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmdf.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmkwm.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmmemory.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmpartitions.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmpci.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcontrol.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/tdmconfig.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/key_bindings.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kfm_home.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/tdescreensaver.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kthememgr.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/licq.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/linuxconf.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/locale.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/preferences-desktop.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/multimedia.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/netscape.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_applications.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-development.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_favourite.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-games.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_games_kids.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-multimedia.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-internet.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_settings.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_toys.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-utilities.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/penguin.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/preferences-desktop-personal.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/phppg.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_games_logic.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/proxy.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/pysol.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/randr.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/samba.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/staroffice.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/stylesheet.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/terminal.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/tux.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/wp.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xclock.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xfmail.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xmag.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xpaint.png
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/access.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/acroread.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/aim.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/aktion.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/antivirus.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/applixware.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/arts.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/background.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/bell.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/browser.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/cache.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/camera.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/clanbomber.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/clock.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/colors.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/core.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/date.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/display.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/download_manager.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/email.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/energy.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/error.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/fifteenpieces.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/filetypes.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/fonts.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/galeon.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/gnome_apps.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/hardware.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/hwinfo.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/ieee1394.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/kcmdevices.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/kcmkwm.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/kcmx.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/locale.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/my_mac.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/netscape.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/openoffice.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/package_development.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/package_games_kids.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/package_toys.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/penguin.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/personal.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/quicktime.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/realplayer.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/samba.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/shell.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/staroffice.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/stylesheet.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/terminal.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/tux.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/wine.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/x.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/xapp.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/xcalc.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/xchat.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/xclock.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/xeyes.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/xpaint.svgz
%{tde_prefix}/share/icons/crystalsvg/*/devices/laptop.png
%{tde_prefix}/share/icons/crystalsvg/*/devices/laptop.svgz
%{tde_prefix}/share/icons/crystalsvg/*/actions/newfont.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/abiword.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/agent.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/alevt.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/assistant.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/blender.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/bluefish.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/cookie.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/designer.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/dia.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/dlgedit.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/eclipse.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/edu_languages.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/edu_mathematics.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/edu_miscellaneous.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-science.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/emacs.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/enhanced_browsing.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/evolution.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/fifteenpieces.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gabber.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gaim.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gnome_apps.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gnomemeeting.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gnucash.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gnumeric.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gv.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gvim.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/icons.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/iconthemes.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/ieee1394.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/preferences-desktop-peripherals.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmkicker.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmmidi.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmprocessor.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmscsi.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmsound.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/preferences-system.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmx.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/keyboard.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/keyboard_layout.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/knotify.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kvirc.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/linguist.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/lyx.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/mac.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/mathematica.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/nedit.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/opera.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_application.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_editors.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_edutainment.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_games_arcade.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_games_board.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_games_card.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_games_strategy.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-graphics.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/package_system.png
%{tde_prefix}/share/icons/crystalsvg/*/categories/applications-office.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/pan.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/panel_settings.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/plan.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/planner.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/pybliographic.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/realplayer.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/remote.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/scribus.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/sodipodi.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/style.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/usb.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/vnc.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/wabi.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/wine.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xcalc.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xchat.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xclipboard.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xconsole.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xedit.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xemacs.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xeyes.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xfig.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xload.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xmms.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xosview.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xv.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/galeon.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmdrkonqi.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/pinguin.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/x.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xapp.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/xawtv.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcmopengl.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/wmaker_apps.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/qtella.png
%{tde_prefix}/share/services/searchproviders
%{tde_prefix}/share/services/useragentstrings/
%{tde_prefix}/share/servicetypes/searchprovider.desktop
%{tde_prefix}/share/servicetypes/uasprovider.desktop
%exclude %{tde_prefix}/share/sounds/pop.wav
%{tde_prefix}/share/sounds/
%{tde_prefix}/share/wallpapers/*

# XDG directories information
%dir %{_sysconfdir}/xdg/menus/applications-merged
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/tde-essential.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-screensavers.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-settings.menu

%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/
%exclude %{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmkonsole/


%package tdeio-plugins
Summary:	Core I/O slaves for TDE
Group:		System/GUI/Other
Requires:	trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	cyrus-sasl
Requires:	psmisc

Obsoletes:	tdebase-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdebase-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdebase-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This package includes the base tdeioslaves. They include, amongst many
others, file, http, and ftp.

It also includes the media tdeioslave, which handles removable devices,
and which works best with udev, udisks and pmount. Media
also extends the functionality of many other tdeioslaves. To use this
service, please make sure that your user is a member of the plugdev
group.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdeio_media_mounthelper
%{tde_prefix}/bin/ktrash
%{tde_prefix}/%{_lib}/trinity/cursorthumbnail.la
%{tde_prefix}/%{_lib}/trinity/cursorthumbnail.so
%{tde_prefix}/%{_lib}/trinity/djvuthumbnail.la
%{tde_prefix}/%{_lib}/trinity/djvuthumbnail.so
%{tde_prefix}/%{_lib}/trinity/htmlthumbnail.la
%{tde_prefix}/%{_lib}/trinity/htmlthumbnail.so
%{tde_prefix}/%{_lib}/trinity/imagethumbnail.la
%{tde_prefix}/%{_lib}/trinity/imagethumbnail.so
%{tde_prefix}/%{_lib}/trinity/kcm_cgi.la
%{tde_prefix}/%{_lib}/trinity/kcm_cgi.so
%{tde_prefix}/%{_lib}/trinity/kcm_media.la
%{tde_prefix}/%{_lib}/trinity/kcm_media.so
%{tde_prefix}/%{_lib}/trinity/kcm_trash.la
%{tde_prefix}/%{_lib}/trinity/kcm_trash.so
%{tde_prefix}/%{_lib}/trinity/kded_homedirnotify.la
%{tde_prefix}/%{_lib}/trinity/kded_homedirnotify.so
%{tde_prefix}/%{_lib}/trinity/kded_mediamanager.la
%{tde_prefix}/%{_lib}/trinity/kded_mediamanager.so
%{tde_prefix}/%{_lib}/trinity/kded_medianotifier.la
%{tde_prefix}/%{_lib}/trinity/kded_medianotifier.so
%{tde_prefix}/%{_lib}/trinity/kded_remotedirnotify.la
%{tde_prefix}/%{_lib}/trinity/kded_remotedirnotify.so
%{tde_prefix}/%{_lib}/trinity/kded_systemdirnotify.la
%{tde_prefix}/%{_lib}/trinity/kded_systemdirnotify.so
%{tde_prefix}/%{_lib}/trinity/tdefile_media.la
%{tde_prefix}/%{_lib}/trinity/tdefile_media.so
%{tde_prefix}/%{_lib}/trinity/tdefile_trash.la
%{tde_prefix}/%{_lib}/trinity/tdefile_trash.so
%{tde_prefix}/%{_lib}/trinity/tdeio_about.la
%{tde_prefix}/%{_lib}/trinity/tdeio_about.so
%{tde_prefix}/%{_lib}/trinity/tdeio_cgi.la
%{tde_prefix}/%{_lib}/trinity/tdeio_cgi.so
%{tde_prefix}/%{_lib}/trinity/tdeio_filter.la
%{tde_prefix}/%{_lib}/trinity/tdeio_filter.so
%{tde_prefix}/%{_lib}/trinity/tdeio_finger.la
%{tde_prefix}/%{_lib}/trinity/tdeio_finger.so
%{tde_prefix}/%{_lib}/trinity/tdeio_fish.la
%{tde_prefix}/%{_lib}/trinity/tdeio_fish.so
%{tde_prefix}/%{_lib}/trinity/tdeio_floppy.la
%{tde_prefix}/%{_lib}/trinity/tdeio_floppy.so
%{tde_prefix}/%{_lib}/trinity/tdeio_home.la
%{tde_prefix}/%{_lib}/trinity/tdeio_home.so
%{tde_prefix}/%{_lib}/trinity/tdeio_info.la
%{tde_prefix}/%{_lib}/trinity/tdeio_info.so
%{tde_prefix}/%{_lib}/trinity/tdeio_mac.la
%{tde_prefix}/%{_lib}/trinity/tdeio_mac.so
%{tde_prefix}/%{_lib}/trinity/tdeio_man.la
%{tde_prefix}/%{_lib}/trinity/tdeio_man.so
%{tde_prefix}/%{_lib}/trinity/tdeio_media.la
%{tde_prefix}/%{_lib}/trinity/tdeio_media.so
%{tde_prefix}/%{_lib}/trinity/tdeio_nfs.la
%{tde_prefix}/%{_lib}/trinity/tdeio_nfs.so
%{tde_prefix}/%{_lib}/trinity/tdeio_remote.la
%{tde_prefix}/%{_lib}/trinity/tdeio_remote.so
%{tde_prefix}/%{_lib}/trinity/tdeio_settings.la
%{tde_prefix}/%{_lib}/trinity/tdeio_settings.so
%if %{with ssh}
%{tde_prefix}/%{_lib}/trinity/tdeio_sftp.la
%{tde_prefix}/%{_lib}/trinity/tdeio_sftp.so
%endif
%{tde_prefix}/%{_lib}/trinity/tdeio_system.la
%{tde_prefix}/%{_lib}/trinity/tdeio_system.so
%{tde_prefix}/%{_lib}/trinity/tdeio_tar.la
%{tde_prefix}/%{_lib}/trinity/tdeio_tar.so
%{tde_prefix}/%{_lib}/trinity/tdeio_thumbnail.la
%{tde_prefix}/%{_lib}/trinity/tdeio_thumbnail.so
%{tde_prefix}/%{_lib}/trinity/tdeio_trash.la
%{tde_prefix}/%{_lib}/trinity/tdeio_trash.so
%{tde_prefix}/%{_lib}/trinity/libkmanpart.la
%{tde_prefix}/%{_lib}/trinity/libkmanpart.so
%{tde_prefix}/%{_lib}/trinity/textthumbnail.la
%{tde_prefix}/%{_lib}/trinity/textthumbnail.so
%{tde_prefix}/share/applications/tde/kcmcgi.desktop
%{tde_prefix}/share/applications/tde/kcmtrash.desktop
%{tde_prefix}/share/apps/tdeio_finger/
%{tde_prefix}/share/apps/tdeio_info/
%{tde_prefix}/share/apps/tdeio_man/
%{tde_prefix}/share/apps/systemview/
%{tde_prefix}/share/autostart/mediabackend.desktop
%{tde_prefix}/share/config.kcfg/mediamanagersettings.kcfg
%{tde_prefix}/share/mimelnk/application/x-smb-server.desktop
%{tde_prefix}/share/mimelnk/inode/system_directory.desktop
%{tde_prefix}/share/mimelnk/media/*.desktop
%{tde_prefix}/share/services/about.protocol
%{tde_prefix}/share/services/applications.protocol
%{tde_prefix}/share/services/ar.protocol
%{tde_prefix}/share/services/bzip.protocol
%{tde_prefix}/share/services/bzip2.protocol
%{tde_prefix}/share/services/cgi.protocol
%{tde_prefix}/share/services/cursorthumbnail.desktop
%{tde_prefix}/share/services/djvuthumbnail.desktop
%{tde_prefix}/share/services/finger.protocol
%{tde_prefix}/share/services/fish.protocol
%{tde_prefix}/share/services/floppy.protocol
%{tde_prefix}/share/services/gzip.protocol
%{tde_prefix}/share/services/home.protocol
%{tde_prefix}/share/services/htmlthumbnail.desktop
%{tde_prefix}/share/services/imagethumbnail.desktop
%{tde_prefix}/share/services/info.protocol
%{tde_prefix}/share/services/kded/homedirnotify.desktop
%{tde_prefix}/share/services/kded/mediamanager.desktop
%{tde_prefix}/share/services/kded/medianotifier.desktop
%{tde_prefix}/share/services/kded/remotedirnotify.desktop
%{tde_prefix}/share/services/kded/systemdirnotify.desktop
%{tde_prefix}/share/services/tdefile_media.desktop
%{tde_prefix}/share/services/tdefile_trash_system.desktop
%{tde_prefix}/share/services/lzma.protocol
%{tde_prefix}/share/services/kmanpart.desktop
%{tde_prefix}/share/services/mac.protocol
%{tde_prefix}/share/services/man.protocol
%{tde_prefix}/share/services/media.protocol
%{tde_prefix}/share/services/nfs.protocol
%{tde_prefix}/share/services/nxfish.protocol
%{tde_prefix}/share/services/programs.protocol
%{tde_prefix}/share/services/remote.protocol
%{tde_prefix}/share/services/settings.protocol
%{?with_ssh:%{tde_prefix}/share/services/sftp.protocol}
%{tde_prefix}/share/services/system.protocol
%{tde_prefix}/share/services/tar.protocol
%{tde_prefix}/share/services/textthumbnail.desktop
%{tde_prefix}/share/services/thumbnail.protocol
%{tde_prefix}/share/services/trash.protocol
%{tde_prefix}/share/services/xz.protocol
%{tde_prefix}/share/services/zip.protocol
%{tde_prefix}/share/servicetypes/thumbcreator.desktop
%{tde_prefix}/share/services/tdefile_trash.desktop
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/
%{tde_prefix}/share/man/man1/ktrash.1*
%{tde_prefix}/share/man/man1/tdeio_media_mounthelper.1*
%if %{with openexr}
%{tde_prefix}/%{_lib}/trinity/exrthumbnail.la
%{tde_prefix}/%{_lib}/trinity/exrthumbnail.so
%{tde_prefix}/share/services/exrthumbnail.desktop
%endif

# HWManager
%{tde_prefix}/%{_lib}/trinity/media_propsdlgplugin.la
%{tde_prefix}/%{_lib}/trinity/media_propsdlgplugin.so
%{tde_prefix}/share/services/media_propsdlgplugin.desktop

%{tde_prefix}/%{_lib}/trinity/ktrashpropsdlgplugin.la
%{tde_prefix}/%{_lib}/trinity/ktrashpropsdlgplugin.so
%{tde_prefix}/share/services/ktrashpropsdlgplugin.desktop

##########

%package -n trinity-tdepasswd
Summary:	Password changer for TDE
Group:		System/GUI/Other

Obsoletes:	trinity-kdepasswd < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdepasswd = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdepasswd
This is a simple application which allows users to change their
system passwords.

%files -n trinity-tdepasswd
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdepasswd
%{tde_prefix}/%{_lib}/trinity/kcm_useraccount.la
%{tde_prefix}/%{_lib}/trinity/kcm_useraccount.so
%{tde_prefix}/share/applications/tde/kcm_useraccount.desktop
%{tde_prefix}/share/applications/tde/tdepasswd.desktop
%{tde_prefix}/share/config.kcfg/kcm_useraccount.kcfg
%{tde_prefix}/share/config.kcfg/kcm_useraccount_pass.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/tdepasswd/
%{_datadir}/faces/Apple.png
%{_datadir}/faces/BeachBall.png
%{_datadir}/faces/Blowfish.png
%{_datadir}/faces/Bug.png
%{_datadir}/faces/Butterfly.png
%{_datadir}/faces/Car.png
%{_datadir}/faces/Cow.png 
%{_datadir}/faces/Daemon.png
%{_datadir}/faces/Dog.png
%{_datadir}/faces/Elephant.png
%{_datadir}/faces/Flower.png
%{_datadir}/faces/Frog.png
%{_datadir}/faces/Ghost.png
%{_datadir}/faces/Guitar.png
%{_datadir}/faces/Heart.png
%{_datadir}/faces/Konqui.png
%{_datadir}/faces/Lion.png
%{_datadir}/faces/Monkey.png
%{_datadir}/faces/Penguin.png
%{_datadir}/faces/Pig.png
%{_datadir}/faces/Rabbit.png
%{_datadir}/faces/Ring.png
%{_datadir}/faces/Scream.png
%{_datadir}/faces/Shark.png
%{_datadir}/faces/Splash.png
%{_datadir}/faces/Star.png
%{_datadir}/faces/Teddybear.png
%{_datadir}/faces/Turtle.png
%{tde_prefix}/share/man/man1/tdepasswd.1*

##########

%package -n trinity-tdeprint
Summary:	Print system for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	psutils

%description -n trinity-tdeprint
This package contains the TDE printing subsystem. It can use CUPS,
lpd-ng or the traditional lpd. It also includes support for fax and
pdf printing.

Installation of smbclient will make you able to use smb shared printers.

%files -n trinity-tdeprint
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdeprintfax
%{tde_prefix}/bin/kjobviewer
%{tde_prefix}/bin/kprinter
%{tde_prefix}/%{_lib}/trinity/kcm_printmgr.la
%{tde_prefix}/%{_lib}/trinity/kcm_printmgr.so
%{tde_prefix}/%{_lib}/trinity/tdeio_print.la
%{tde_prefix}/%{_lib}/trinity/tdeio_print.so
%{tde_prefix}/%{_lib}/trinity/kjobviewer.la
%{tde_prefix}/%{_lib}/trinity/kjobviewer.so
%{tde_prefix}/%{_lib}/trinity/kprinter.la
%{tde_prefix}/%{_lib}/trinity/kprinter.so
%{tde_prefix}/%{_lib}/trinity/libtdeprint_part.la
%{tde_prefix}/%{_lib}/trinity/libtdeprint_part.so
%{tde_prefix}/%{_lib}/libtdeinit_kjobviewer.la
%{tde_prefix}/%{_lib}/libtdeinit_kjobviewer.so
%{tde_prefix}/%{_lib}/libtdeinit_kprinter.la
%{tde_prefix}/%{_lib}/libtdeinit_kprinter.so
%{tde_prefix}/share/applications/tde/tdeprintfax.desktop
%{tde_prefix}/share/applications/tde/kjobviewer.desktop
%{tde_prefix}/share/applications/tde/printers.desktop
%{tde_prefix}/share/apps/tdeprint/
%{tde_prefix}/share/apps/tdeprintfax/
%{tde_prefix}/share/apps/kjobviewer/
%{tde_prefix}/share/apps/tdeprint_part/
%{tde_prefix}/share/autostart/kjobviewer-autostart.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/tdeprintfax.png
%{tde_prefix}/share/icons/hicolor/*/apps/kjobviewer.png
%{tde_prefix}/share/icons/hicolor/*/apps/printmgr.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/tdeprintfax.svgz
%{tde_prefix}/share/icons/hicolor/scalable/apps/kjobviewer.svgz
%{tde_prefix}/share/icons/hicolor/scalable/apps/printmgr.svgz
%{tde_prefix}/share/mimelnk/print/class.desktop
%{tde_prefix}/share/mimelnk/print/driver.desktop
%{tde_prefix}/share/mimelnk/print/folder.desktop
%{tde_prefix}/share/mimelnk/print/jobs.desktop
%{tde_prefix}/share/mimelnk/print/manager.desktop
%{tde_prefix}/share/mimelnk/print/printer.desktop
%{tde_prefix}/share/mimelnk/print/printermodel.desktop
%{tde_prefix}/share/services/tdeprint_part.desktop
%{tde_prefix}/share/services/print.protocol
%{tde_prefix}/share/services/printdb.protocol
%{tde_prefix}/share/doc/tde/HTML/en/tdeprint/
%{tde_prefix}/share/doc/tde/HTML/en/tdeprintfax/
%{tde_prefix}/share/doc/tde/HTML/en/kjobviewer/
%{tde_prefix}/share/man/man1/kjobviewer.1*
%{tde_prefix}/share/man/man1/kprinter.1*
%{tde_prefix}/share/man/man1/tdeprintfax.1*

##########

%package -n trinity-kdesktop
Summary:	Miscellaneous binaries and files for the TDE desktop
Group:		System/GUI/Other
Requires:	%{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	eject
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
Requires:	xdg-utils
%endif

%description -n trinity-kdesktop
This package contains miscellaneous binaries and files integral to
the TDE desktop.

%files -n trinity-kdesktop
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kdesktop_custom_menu1
%config(noreplace) %{_sysconfdir}/trinity/kdesktop_custom_menu2
%{tde_prefix}/bin/kcheckrunning
%{tde_prefix}/bin/tdeeject
%{tde_prefix}/bin/kdesktop
%{tde_prefix}/bin/kdesktop_lock
%{tde_prefix}/bin/kwebdesktop
%{tde_prefix}/%{_lib}/trinity/kdesktop.la
%{tde_prefix}/%{_lib}/trinity/kdesktop.so
%{tde_prefix}/%{_lib}/libtdeinit_kdesktop.la
%{tde_prefix}/%{_lib}/libtdeinit_kdesktop.so
%{tde_prefix}/share/apps/kdesktop/
%{tde_prefix}/share/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%{tde_prefix}/share/autostart/kdesktop.desktop
%{tde_prefix}/share/config.kcfg/kdesktop.kcfg
%{tde_prefix}/share/config.kcfg/tdelaunch.kcfg
%{tde_prefix}/share/config.kcfg/kwebdesktop.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/error.png

##########

%package -n trinity-kdesktop-devel
Summary:	Development files for kdesktop
Group:		Development/Libraries/Other
Requires:	trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kdesktop-devel
This package contains the development files for kdesktop.

%files -n trinity-kdesktop-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/KBackgroundIface.h
%{tde_prefix}/include/tde/KDesktopIface.h
%{tde_prefix}/include/tde/KScreensaverIface.h

##########

%package -n trinity-tdm
Summary:	X Display manager for TDE
Group:		System/GUI/Other
Requires:	%{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	pam
Requires:	logrotate

# Provides the global Xsession script (/etc/X11/xinit/Xsession or /etc/X11/Xsession)
Requires:	xinitrc
Provides:	dm
Provides:	tdm

%description -n trinity-tdm
TDM manages a collection of X servers, which may be on the local host or
remote machines. It provides services similar to those provided by init,
getty, and login on character-based terminals: prompting for login name and
password, authenticating the user, and running a session. tdm supports XDMCP
(X Display Manager Control Protocol) and can also be used to run a chooser
process which presents the user with a menu of possible hosts that offer
XDMCP display management.

A collection of icons to associate with individual users is included with
TDE, but as part of the tdepasswd package.

The menu package will help to provide TDM with a list of window managers
that can be launched, if the window manager does not register with TDM
already. Most users won't need this.

%files -n trinity-tdm
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kgreet_pam.la
%{tde_prefix}/%{_lib}/trinity/kgreet_pam.so
%{tde_prefix}/bin/gentdmconf
%{tde_prefix}/bin/tdm
%{tde_prefix}/bin/tdm_config
%{tde_prefix}/bin/tdmctl
%{tde_prefix}/bin/tdm_greet
%{tde_prefix}/bin/krootimage
%dir %{tde_prefix}/share/apps/tdm
%dir %{tde_prefix}/share/apps/tdm/pics
%{tde_prefix}/share/apps/tdm/pics/tdelogo.png
%{tde_prefix}/share/apps/tdm/pics/shutdown.jpg
%{tde_prefix}/share/apps/tdm/pics/users
%dir %{tde_prefix}/share/apps/tdm/sessions
%{tde_prefix}/share/apps/tdm/sessions/*.desktop
%{tde_prefix}/share/apps/tdm/themes/
%config(noreplace) %{_sysconfdir}/trinity/tdm
%{tde_prefix}/share/doc/tde/HTML/en/tdm/
%config(noreplace) %{_sysconfdir}/pam.d/tdm-trinity
%config(noreplace) %{_sysconfdir}/pam.d/tdm-trinity-np
%{tde_prefix}/share/man/man1/gentdmconf.1*
%{tde_prefix}/share/man/man1/krootimage.1*
%{tde_prefix}/share/man/man1/tdm.1*
%{tde_prefix}/share/man/man1/tdmctl.1*
%{tde_prefix}/share/man/man1/tdm_config.1*
%{tde_prefix}/share/man/man1/tdm_greet.1*
%{tde_prefix}/bin/tdecryptocardwatcher

# XDG user faces
%dir %{_datadir}/faces
%{_datadir}/faces/default1.png
%{_datadir}/faces/default2.png
%{_datadir}/faces/default3.png
%{_datadir}/faces/default4.png
%{_datadir}/faces/root1.png

# Distribution specific stuff
%{?with_systemd:%{_unitdir}/tdm.service}
%{_datadir}/xsessions/tde.desktop

%{_sysconfdir}/X11/wmsession.d/45TDE
%{_datadir}/X11/dm.d/45TDE.conf

# Logrotate configuration
%config %{_sysconfdir}/logrotate.d/trinity-tdm

%pre -n trinity-tdm
# Make sure that TDM configuration files are now under '/etc/trinity/tdm'
if [ -d "%{tde_prefix}/share/config/tdm" ] && [ ! -L "%{tde_prefix}/share/config/tdm" ]; then
  if [ -d "%{_sysconfdir}/trinity/tdm" ]; then
    # If there is already something under '/etc/trinity/tdm', simply delete old configuration
    echo "Deleting TDM configuration under '%{tde_prefix}/share/config/tdm'"
    rm -rf "%{tde_prefix}/share/config/tdm"
  else
    # Else, move '/opt/trinity/share/config/tdm' to '/etc/trinity/tdm'
    if [ ! -d "%{_sysconfdir}/trinity" ]; then
      mkdir -p "%{_sysconfdir}/trinity"
    fi
    echo "Migrating TDM configuration from '%{tde_prefix}/share/config/tdm' to '%{_sysconfdir}/trinity/tdm'"
    mv -f "%{tde_prefix}/share/config/tdm" "%{_sysconfdir}/trinity/tdm.migr"
  fi
fi

# Remove actual directory before creating a symlink
if [ ! -L "%{tde_prefix}/share/apps/tdm/pics/users" ] && [ -d "%{tde_prefix}/share/apps/tdm/pics/users" ] ; then
  [ -d "%{_datadir}/faces" ] || mkdir -p "%{_datadir}/faces"
  cp -f "%{tde_prefix}/share/apps/tdm/pics/users/"* "%{_datadir}/faces"
  rm -rf "%{tde_prefix}/share/apps/tdm/pics/users"
fi

%post -n trinity-tdm
%make_session

# Sets default user icon in TDM
if [ ! -r "%{tde_prefix}/share/apps/tdm/faces/.default.face.icon" ]; then
  [ -d "%{tde_prefix}/share/apps/tdm/faces" ] || mkdir -p "%{tde_prefix}/share/apps/tdm/faces"
  cp -f "%{tde_prefix}/share/apps/tdm/pics/users/default2.png" "%{tde_prefix}/share/apps/tdm/faces/.default.face.icon"
fi

# Sets default language for TDM
if [ "$1" = "1" ]; then
  if [ -n "${LANG}" ] && [ "${LANG}" != "C" ]; then
    sed -i "%{_sysconfdir}/trinity/tdm/tdmrc" -e "s|^#*Language=.*|Language=${LANG}|"
  fi
fi

%posttrans -n trinity-tdm
# Make sure that TDM configuration files are now under '/etc/trinity/tdm'
if [ -d "%{_sysconfdir}/trinity/tdm.migr" ] && [ -d "%{_sysconfdir}/trinity/tdm" ]; then
  mv -f "%{_sysconfdir}/trinity/tdm.migr/"* "%{_sysconfdir}/trinity/tdm/"
  rmdir "%{_sysconfdir}/trinity/tdm.migr/"
fi

%postun -n trinity-tdm
%make_session

%package -n trinity-tdm-devel
Summary:	Development files for tdm
Group:		Development/Libraries/Other
Requires:	trinity-tdm = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

%description -n trinity-tdm-devel
This package contains the development files for TDM.

%files -n trinity-tdm-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kgreeterplugin.h

##########

%package -n trinity-kfind
Summary:	File-find utility for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kfind
kfind can be used to find files and directories on your
workstations.

%files -n trinity-kfind
%defattr(-,root,root,-)
%{tde_prefix}/bin/kfind
%{tde_prefix}/%{_lib}/trinity/libkfindpart.la
%{tde_prefix}/%{_lib}/trinity/libkfindpart.so
%{tde_prefix}/share/applications/tde/Kfind.desktop
%{tde_prefix}/share/apps/kfindpart/
%{tde_prefix}/share/icons/hicolor/*/apps/kfind.png
%{tde_prefix}/share/services/kfindpart.desktop
%{tde_prefix}/share/servicetypes/findpart.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kfind/
%{tde_prefix}/share/man/man1/kfind.1*

##########

%package -n trinity-khelpcenter
Summary:	Help center for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	htdig

%description -n trinity-khelpcenter
The TDE Help Center provides documentation on how to use the TDE desktop.

The htdig package is needed to build a searchable archive of TDE
documentation.

%files -n trinity-khelpcenter
%defattr(-,root,root,-)
%{tde_prefix}/bin/khc_docbookdig.pl
%{tde_prefix}/bin/khc_htdig.pl
%{tde_prefix}/bin/khc_htsearch.pl
%{tde_prefix}/bin/khc_indexbuilder
%{tde_prefix}/bin/khc_mansearch.pl
%{tde_prefix}/bin/khelpcenter
%{tde_prefix}/%{_lib}/trinity/khelpcenter.la
%{tde_prefix}/%{_lib}/trinity/khelpcenter.so
%{tde_prefix}/%{_lib}/libtdeinit_khelpcenter.la
%{tde_prefix}/%{_lib}/libtdeinit_khelpcenter.so
%{tde_prefix}/share/applications/tde/Help.desktop
%{tde_prefix}/share/apps/khelpcenter/
%{tde_prefix}/share/config.kcfg/khelpcenter.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/khelpcenter.*
%{tde_prefix}/share/services/khelpcenter.desktop
%{tde_prefix}/share/doc/tde/HTML/en/khelpcenter/

##########

%package -n trinity-kicker
Summary:	Desktop panel for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kicker
Kicker provides the TDE panel on you desktop. It can be used as a
program launcher and can load plugins to provide additional
functionality.

%files -n trinity-kicker
%defattr(-,root,root,-)
%{tde_prefix}/bin/appletproxy
%{tde_prefix}/bin/extensionproxy
%{tde_prefix}/bin/kasbar
%{tde_prefix}/bin/kicker
%{tde_prefix}/%{_lib}/tdeconf_update_bin/kicker-3.4-reverseLayout
%{tde_prefix}/%{_lib}/trinity/appletproxy.la
%{tde_prefix}/%{_lib}/trinity/appletproxy.so
%{tde_prefix}/%{_lib}/trinity/clock_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/clock_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/dockbar_panelextension.la
%{tde_prefix}/%{_lib}/trinity/dockbar_panelextension.so
%{tde_prefix}/%{_lib}/trinity/extensionproxy.la
%{tde_prefix}/%{_lib}/trinity/extensionproxy.so
%{tde_prefix}/%{_lib}/trinity/kasbar_panelextension.la
%{tde_prefix}/%{_lib}/trinity/kasbar_panelextension.so
%{tde_prefix}/%{_lib}/trinity/kicker.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_find.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_find.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_kate.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_kate.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_tdeprint.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_tdeprint.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_konqueror.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_konqueror.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_konsole.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_konsole.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_prefmenu.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_prefmenu.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_recentdocs.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_recentdocs.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_remotemenu.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_remotemenu.so
%{tde_prefix}/%{_lib}/trinity/kickermenu_systemmenu.la
%{tde_prefix}/%{_lib}/trinity/kickermenu_systemmenu.so
%{tde_prefix}/%{_lib}/trinity/kicker.so
%{tde_prefix}/%{_lib}/trinity/launcher_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/launcher_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/lockout_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/lockout_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/media_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/media_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/menu_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/menu_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/minipager_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/minipager_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/naughty_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/naughty_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/run_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/run_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/sidebar_panelextension.la
%{tde_prefix}/%{_lib}/trinity/sidebar_panelextension.so
%{tde_prefix}/%{_lib}/trinity/systemtray_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/systemtray_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/taskbar_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/taskbar_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/taskbar_panelextension.la
%{tde_prefix}/%{_lib}/trinity/taskbar_panelextension.so
%{tde_prefix}/%{_lib}/trinity/trash_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/trash_panelapplet.so
%{tde_prefix}/%{_lib}/libkasbar.so.*
%{tde_prefix}/%{_lib}/libtdeinit_appletproxy.la
%{tde_prefix}/%{_lib}/libtdeinit_appletproxy.so
%{tde_prefix}/%{_lib}/libtdeinit_extensionproxy.la
%{tde_prefix}/%{_lib}/libtdeinit_extensionproxy.so
%{tde_prefix}/%{_lib}/libtdeinit_kicker.la
%{tde_prefix}/%{_lib}/libtdeinit_kicker.so
%{tde_prefix}/%{_lib}/libkickermain.so.*
%{tde_prefix}/%{_lib}/libtaskbar.so.*
%{tde_prefix}/%{_lib}/libtaskmanager.so.*
%{tde_prefix}/%{_lib}/libkickoffsearch_interfaces.so.*
%{tde_prefix}/share/applications/tde/kcmkicker.desktop
%{tde_prefix}/share/applnk/.hidden/kicker_config_arrangement.desktop
%{tde_prefix}/share/applnk/.hidden/kicker_config_hiding.desktop
%{tde_prefix}/share/applnk/.hidden/kicker_config_menus.desktop
%{tde_prefix}/share/apps/clockapplet/
%{tde_prefix}/share/apps/tdeconf_update/kicker-3.1-properSizeSetting.pl
%{tde_prefix}/share/apps/tdeconf_update/kicker-3.5-taskbarEnums.pl
%{tde_prefix}/share/apps/tdeconf_update/kickerrc.upd
%{tde_prefix}/share/apps/kicker/
%exclude %{tde_prefix}/share/apps/kicker/applets/klipper.desktop
%exclude %{tde_prefix}/share/apps/kicker/applets/ksysguardapplet.desktop
%{tde_prefix}/share/apps/naughtyapplet/
%{tde_prefix}/share/autostart/panel.desktop
%{tde_prefix}/share/config.kcfg/kickerSettings.kcfg
%{tde_prefix}/share/config.kcfg/launcherapplet.kcfg
%{tde_prefix}/share/config.kcfg/pagersettings.kcfg
%{tde_prefix}/share/config.kcfg/taskbar.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/systemtray.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/taskbar.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kbinaryclock.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kdisknav.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kicker.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/panel.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/runprocesscatcher.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kbinaryclock.svgz
%{tde_prefix}/share/icons/crystalsvg/*/apps/systemtray.svgz
%{tde_prefix}/share/servicetypes/kickoffsearchplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kicker/
%{tde_prefix}/share/man/man1/appletproxy.1*
%{tde_prefix}/share/man/man1/extensionproxy.1*
%{tde_prefix}/share/man/man1/kasbar.1*
%{tde_prefix}/share/man/man1/kicker.1*

##########

%package -n trinity-kicker-devel
Summary:	Development files for kicker
Group:		Development/Libraries/Other
Requires:	trinity-kicker = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

%description -n trinity-kicker-devel
This package contains the development files for kicker.

%files -n trinity-kicker-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kickoff-search-plugin.h
%{tde_prefix}/include/tde/kickoffsearchinterface.h
%{tde_prefix}/%{_lib}/libkasbar.la
%{tde_prefix}/%{_lib}/libkasbar.so
%{tde_prefix}/%{_lib}/libkickermain.la
%{tde_prefix}/%{_lib}/libkickermain.so
%{tde_prefix}/%{_lib}/libkickoffsearch_interfaces.la
%{tde_prefix}/%{_lib}/libkickoffsearch_interfaces.so
%{tde_prefix}/%{_lib}/libtaskbar.la
%{tde_prefix}/%{_lib}/libtaskbar.so
%{tde_prefix}/%{_lib}/libtaskmanager.la
%{tde_prefix}/%{_lib}/libtaskmanager.so

##########

%package -n trinity-klipper
Summary:	Clipboard utility for Trinity
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-klipper
klipper provides standard clipboard functions (cut and paste, history
saving) plus additional features, like the ability to offer actions to 
take dependent on the clipboard contents. For example, it can launch a 
web browser if the clipboard contains a URL.

%files -n trinity-klipper
%defattr(-,root,root,-)
%{tde_prefix}/bin/klipper
%config(noreplace) %{_sysconfdir}/trinity/klipperrc
%{tde_prefix}/%{_lib}/trinity/klipper.la
%{tde_prefix}/%{_lib}/trinity/klipper.so
%{tde_prefix}/%{_lib}/trinity/klipper_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/klipper_panelapplet.so
%{tde_prefix}/%{_lib}/libtdeinit_klipper.la
%{tde_prefix}/%{_lib}/libtdeinit_klipper.so
%{tde_prefix}/share/applications/tde/klipper.desktop
%{tde_prefix}/share/apps/tdeconf_update/klipper-1-2.pl
%{tde_prefix}/share/apps/tdeconf_update/klipper-trinity1.sh
%{tde_prefix}/share/apps/tdeconf_update/klipperrc.upd
%{tde_prefix}/share/apps/tdeconf_update/klippershortcuts.upd
%{tde_prefix}/share/apps/kicker/applets/klipper.desktop
%{tde_prefix}/share/autostart/klipper.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/klipper.*
%{tde_prefix}/share/doc/tde/HTML/en/klipper/

##########

%package -n trinity-kmenuedit
Summary:	Menu editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kmenuedit
The TDE menu editor allows you to make customisations to the TDE menu
structure.

%files -n trinity-kmenuedit
%defattr(-,root,root,-)
%{tde_prefix}/bin/kcontroledit
%{tde_prefix}/bin/kmenuedit
%{tde_prefix}/%{_lib}/trinity/kcontroledit.la
%{tde_prefix}/%{_lib}/trinity/kcontroledit.so
%{tde_prefix}/%{_lib}/trinity/kmenuedit.la
%{tde_prefix}/%{_lib}/trinity/kmenuedit.so
%{tde_prefix}/%{_lib}/libtdeinit_kcontroledit.la
%{tde_prefix}/%{_lib}/libtdeinit_kcontroledit.so
%{tde_prefix}/%{_lib}/libtdeinit_kmenuedit.la
%{tde_prefix}/%{_lib}/libtdeinit_kmenuedit.so
%{tde_prefix}/share/applications/tde/kmenuedit.desktop
%{tde_prefix}/share/applnk/System/kmenuedit.desktop
%{tde_prefix}/share/apps/kcontroledit/
%{tde_prefix}/share/apps/kmenuedit/
%{tde_prefix}/share/doc/tde/HTML/en/kmenuedit/
%{tde_prefix}/share/man/man1/kmenuedit.1*

##########

%package -n trinity-konqueror
Summary:	TDE's advanced file manager, web browser and document viewer
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kcontrol = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kfind = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konqueror
Konqueror is the file manager for the Trinity Desktop Environment.
It supports basic file management on local UNIX filesystems,
from simple cut/copy and paste operations to advanced remote
and local network file browsing.

It is also the canvas for all the latest TDE technology,
from KIO slaves (which provide mechanisms for file access) to
component embedding via the KParts object interface, and it
is one of the most customizable applications available.

Konqueror is an Open Source web browser with HTML4.0 compliance,
supporting Java applets, JavaScript, CSS1 and (partially) CSS2,
as well as Netscape plugins (for example, Flash or RealVideo plugins).

It is a universal viewing application, capable of embedding
read-only viewing components in itself to view documents without
ever launching another application.

%files -n trinity-konqueror
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/konqsidebartng.rc
%{tde_prefix}/bin/kbookmarkmerger
%{tde_prefix}/bin/keditbookmarks
%{tde_prefix}/bin/kfmclient
%{tde_prefix}/bin/konqueror
%{tde_prefix}/%{_lib}/trinity/kcm_history.la
%{tde_prefix}/%{_lib}/trinity/kcm_history.so
%{tde_prefix}/%{_lib}/trinity/kded_konqy_preloader.la
%{tde_prefix}/%{_lib}/trinity/kded_konqy_preloader.so
%{tde_prefix}/%{_lib}/trinity/keditbookmarks.la
%{tde_prefix}/%{_lib}/trinity/keditbookmarks.so
%{tde_prefix}/%{_lib}/trinity/kfmclient.la
%{tde_prefix}/%{_lib}/trinity/kfmclient.so
%{tde_prefix}/%{_lib}/trinity/konq_aboutpage.la
%{tde_prefix}/%{_lib}/trinity/konq_aboutpage.so
%{tde_prefix}/%{_lib}/trinity/konq_iconview.la
%{tde_prefix}/%{_lib}/trinity/konq_iconview.so
%{tde_prefix}/%{_lib}/trinity/konq_listview.la
%{tde_prefix}/%{_lib}/trinity/konq_listview.so
%{tde_prefix}/%{_lib}/trinity/konq_remoteencoding.la
%{tde_prefix}/%{_lib}/trinity/konq_remoteencoding.so
%{tde_prefix}/%{_lib}/trinity/konq_shellcmdplugin.la
%{tde_prefix}/%{_lib}/trinity/konq_shellcmdplugin.so
%{tde_prefix}/%{_lib}/trinity/konq_sidebar.la
%{tde_prefix}/%{_lib}/trinity/konq_sidebar.so
%{tde_prefix}/%{_lib}/trinity/konq_sidebartree_bookmarks.la
%{tde_prefix}/%{_lib}/trinity/konq_sidebartree_bookmarks.so
%{tde_prefix}/%{_lib}/trinity/konq_sidebartree_dirtree.la
%{tde_prefix}/%{_lib}/trinity/konq_sidebartree_dirtree.so
%{tde_prefix}/%{_lib}/trinity/konq_sidebartree_history.la
%{tde_prefix}/%{_lib}/trinity/konq_sidebartree_history.so
%{tde_prefix}/%{_lib}/trinity/konqsidebar_tree.la
%{tde_prefix}/%{_lib}/trinity/konqsidebar_tree.so
%{tde_prefix}/%{_lib}/trinity/konqsidebar_web.la
%{tde_prefix}/%{_lib}/trinity/konqsidebar_web.so
%{tde_prefix}/%{_lib}/trinity/konqueror.la
%{tde_prefix}/%{_lib}/trinity/konqueror.so
%{tde_prefix}/%{_lib}/trinity/libtdehtmlkttsdplugin.la
%{tde_prefix}/%{_lib}/trinity/libtdehtmlkttsdplugin.so
%{tde_prefix}/%{_lib}/libtdeinit_keditbookmarks.la
%{tde_prefix}/%{_lib}/libtdeinit_keditbookmarks.so
%{tde_prefix}/%{_lib}/libtdeinit_kfmclient.la
%{tde_prefix}/%{_lib}/libtdeinit_kfmclient.so
%{tde_prefix}/%{_lib}/libtdeinit_konqueror.la
%{tde_prefix}/%{_lib}/libtdeinit_konqueror.so
%{tde_prefix}/%{_lib}/libkonqsidebarplugin.so.*
%{tde_prefix}/share/applications/tde/Home.desktop
%{tde_prefix}/share/applications/tde/kcmhistory.desktop
%{tde_prefix}/share/applications/tde/kfmclient.desktop
%{tde_prefix}/share/applications/tde/kfmclient_dir.desktop
%{tde_prefix}/share/applications/tde/kfmclient_html.desktop
%{tde_prefix}/share/applications/tde/kfmclient_war.desktop
%{tde_prefix}/share/applications/tde/tdehtml_filter.desktop
%{tde_prefix}/share/applications/tde/konqbrowser.desktop
%{tde_prefix}/share/applications/tde/konquerorsu.desktop
%{tde_prefix}/share/applnk/.hidden/konqfilemgr.desktop
%{tde_prefix}/share/applnk/Internet/keditbookmarks.desktop
%{tde_prefix}/share/applnk/konqueror.desktop
%{tde_prefix}/share/apps/tdeconf_update/kfmclient_3_2.upd
%{tde_prefix}/share/apps/tdeconf_update/kfmclient_3_2_update.sh
%{tde_prefix}/share/apps/tdeconf_update/konqsidebartng.upd
%{tde_prefix}/share/apps/tdeconf_update/move_konqsidebartng_entries.sh
%{tde_prefix}/share/apps/keditbookmarks/
%{tde_prefix}/share/apps/tdehtml/kpartplugins/
%{tde_prefix}/share/apps/konqiconview/
%{tde_prefix}/share/apps/konqlistview/
%exclude %{tde_prefix}/share/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{tde_prefix}/share/apps/konqsidebartng/
%{tde_prefix}/share/apps/konqueror/about/
%dir %{tde_prefix}/share/apps/konqueror/dirtree
%dir %{tde_prefix}/share/apps/konqueror/dirtree/remote
%{tde_prefix}/share/apps/konqueror/icons/
%{tde_prefix}/share/apps/konqueror/konq-simplebrowser.rc
%{tde_prefix}/share/apps/konqueror/konqueror.rc
%{tde_prefix}/share/apps/konqueror/pics/indicator_connect.png
%{tde_prefix}/share/apps/konqueror/pics/indicator_empty.png
%{tde_prefix}/share/apps/konqueror/pics/indicator_noconnect.png
%{tde_prefix}/share/apps/konqueror/pics/indicator_viewactive.png
%{tde_prefix}/share/apps/konqueror/profiles/
%exclude %{tde_prefix}/share/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%exclude %{tde_prefix}/share/apps/konqueror/servicemenus/installfont.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/*.desktop
%ghost %{_sysconfdir}/alternatives/media_safelyremove.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase
%{tde_prefix}/share/apps/konqueror/tiles/
%{tde_prefix}/share/autostart/konqy_preload.desktop
%{tde_prefix}/share/config.kcfg/keditbookmarks.kcfg
%{tde_prefix}/share/config.kcfg/konq_listview.kcfg
%{tde_prefix}/share/config.kcfg/konqueror.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/keditbookmarks.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kfm_home.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/kfm.png
%{tde_prefix}/share/icons/hicolor/*/apps/konqueror.*
%{tde_prefix}/share/services/kded/konqy_preloader.desktop
%{tde_prefix}/share/services/konq_*.desktop
%{tde_prefix}/share/servicetypes/konqaboutpage.desktop
%{tde_prefix}/share/doc/tde/HTML/en/konqueror/
%{tde_prefix}/share/doc/tde/HTML/en/keditbookmarks/
%{tde_prefix}/share/man/man1/keditbookmarks.1*
%{tde_prefix}/share/man/man1/kfmclient.1*
%{tde_prefix}/share/man/man1/konqueror.1*

%post -n trinity-konqueror
if [ $1 -eq 1 ]; then
  update-alternatives --install \
    %{tde_prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop \
    media_safelyremove.desktop_konqueror \
    %{tde_prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase \
    10 || :
fi

%preun -n trinity-konqueror
if [ $1 -eq 0 ]; then
  update-alternatives --remove \
    media_safelyremove.desktop_konqueror \
    %{tde_prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase || :
fi

##########

%package -n trinity-konqueror-devel
Summary:	Development files for konqueror
Group:		Development/Libraries/Other
Requires:	trinity-konqueror = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konqueror-devel
This package contains the development files for konqueror.

%files -n trinity-konqueror-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/konqsidebarplugin.h
%{tde_prefix}/include/tde/KonquerorIface.h
%{tde_prefix}/%{_lib}/libkonqsidebarplugin.la
%{tde_prefix}/%{_lib}/libkonqsidebarplugin.so

##########

%package -n trinity-konqueror-nsplugins
Summary:	Netscape plugin support for Konqueror
Group:		System/GUI/Other
Requires:	trinity-konqueror = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konqueror-nsplugins
This package includes support for Netscape plugins in Konqueror.

%files -n trinity-konqueror-nsplugins
%defattr(-,root,root,-)
%{tde_prefix}/bin/nspluginscan
%{tde_prefix}/bin/nspluginviewer
%{tde_prefix}/%{_lib}/trinity/kcm_nsplugins.la
%{tde_prefix}/%{_lib}/trinity/kcm_nsplugins.so
%{tde_prefix}/%{_lib}/trinity/libnsplugin.la
%{tde_prefix}/%{_lib}/trinity/libnsplugin.so
%{tde_prefix}/share/applications/tde/tdehtml_plugins.desktop
%{tde_prefix}/share/apps/plugin/nspluginpart.rc

##########

%package -n trinity-konsole
Summary:	X terminal emulator for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konsole
Konsole is an X terminal emulation which provides a command-line interface
(CLI) while using the graphical Trinity Desktop Environment. Konsole helps to
better organize user's desktop by containing multiple sessions in a single
window (a less cluttered desktop).

Its advanced features include a simple configuration and the ability to use
multiple terminal shells in a single window

Using Konsole, a user can open:
* Linux console sessions
* Midnight Commander file manager sessions
* Shell sessions
* Root consoles sessions

%files -n trinity-konsole
%defattr(-,root,root,-)
%{tde_prefix}/bin/konsole
%{tde_prefix}/bin/terminalhere
%{tde_prefix}/%{_lib}/trinity/kcm_konsole.la
%{tde_prefix}/%{_lib}/trinity/kcm_konsole.so
%{tde_prefix}/%{_lib}/trinity/kded_kwrited.la
%{tde_prefix}/%{_lib}/trinity/kded_kwrited.so
%{tde_prefix}/%{_lib}/trinity/konsole.la
%{tde_prefix}/%{_lib}/trinity/konsole.so
%{tde_prefix}/%{_lib}/trinity/libkonsolepart.la
%{tde_prefix}/%{_lib}/trinity/libkonsolepart.so
%{tde_prefix}/%{_lib}/libtdeinit_konsole.la
%{tde_prefix}/%{_lib}/libtdeinit_konsole.so
%{tde_prefix}/share/applications/tde/konsole.desktop
%{tde_prefix}/share/applications/tde/konsolesu.desktop
%{tde_prefix}/share/applnk/.hidden/kcmkonsole.desktop
%{tde_prefix}/share/apps/tdeconf_update/konsole.upd
%{tde_prefix}/share/apps/tdeconf_update/schemaStrip.pl
%{tde_prefix}/share/apps/konsole/
%{tde_prefix}/share/icons/hicolor/*/apps/konsole.*
%{tde_prefix}/share/mimelnk/application/x-konsole.desktop
%{tde_prefix}/share/services/kded/kwrited.desktop
%{tde_prefix}/share/services/konsolepart.desktop
%{tde_prefix}/share/services/konsole-script.desktop
%{tde_prefix}/share/services/kwrited.desktop
%{tde_prefix}/share/servicetypes/terminalemulator.desktop
%{tde_prefix}/share/doc/tde/HTML/en/konsole/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmkonsole/
%config %{_sysconfdir}/fonts/conf.d/99-konsole.conf
%{tde_prefix}/share/man/man1/konsole.1*

##########

%package -n trinity-kpager
Summary:	Desktop pager for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kpager
This package contains TDE's desktop pager, which displays your virtual
desktops iconically in a window, along with icons of any running
applications. It is used to switch between applications or desktops.

%files -n trinity-kpager
%defattr(-,root,root,-)
%{tde_prefix}/bin/kpager
%{tde_prefix}/share/applications/tde/kpager.desktop
%{tde_prefix}/share/applnk/Utilities/kpager.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kpager.png
%{tde_prefix}/share/doc/tde/HTML/en/kpager/
%{tde_prefix}/share/man/man1/kpager.1*

##########

%package -n trinity-kpersonalizer
Summary:	Installation personalizer for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kpersonalizer
TDE Personalizer is the application that configures the TDE desktop for you.
It's a very useful wizard that allows you to quickly change the TDE desktop to
suit your own needs. When you run TDE for the first time, KPersonalizer is
automatically started. KPersonalizer can also be called later.

%files -n trinity-kpersonalizer
%defattr(-,root,root,-)
%{tde_prefix}/bin/kpersonalizer
%{tde_prefix}/share/applications/tde/kpersonalizer.desktop
%{tde_prefix}/share/applnk/System/kpersonalizer.desktop
%{tde_prefix}/share/apps/kpersonalizer/
%{tde_prefix}/share/icons/crystalsvg/*/apps/kpersonalizer.png
%{tde_prefix}/share/man/man1/kpersonalizer.1*

##########

%package -n trinity-ksmserver
Summary:	Session manager for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-twin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	xmessage
Requires:	xprop

%description -n trinity-ksmserver
This package contains the TDE session manager. It is responsible for
restoring your TDE session on login. It is also needed to properly
start a TDE session. It registers TDE with X display managers, and
provides the 'starttde' command, for starting an X session with TDE
from the console.

If you are running TDE for the first time for a certain user,
kpersonalizer is used to help with setup. If it is not present,
TDE will start, but many good defaults will not be set.

%files -n trinity-ksmserver
%defattr(-,root,root,-)
%{tde_prefix}/bin/ksmserver
%{tde_prefix}/bin/starttde
%{tde_prefix}/bin/migratekde3
%{tde_prefix}/bin/r14-xdg-update
%{tde_prefix}/bin/tdeinit_displayconfig
%{tde_prefix}/bin/tdeinit_phase1
%{tde_prefix}/%{_lib}/trinity/ksmserver.la
%{tde_prefix}/%{_lib}/trinity/ksmserver.so
%{tde_prefix}/%{_lib}/libtdeinit_ksmserver.la
%{tde_prefix}/%{_lib}/libtdeinit_ksmserver.so
%{tde_prefix}/share/apps/tdeconf_update/ksmserver.upd
%{tde_prefix}/share/apps/tdeconf_update/move_session_config.sh
%{tde_prefix}/share/apps/ksmserver/
%{tde_prefix}/share/man/man1/starttde.1*


##########

%package -n trinity-ksplash
Summary:	The TDE splash screen
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksplash
This package includes the TDE Splash screen, which is seen when
a TDE session is launched.

%files -n trinity-ksplash
%defattr(-,root,root,-)
%{tde_prefix}/bin/ksplash
%{tde_prefix}/bin/ksplashsimple
%{tde_prefix}/%{_lib}/trinity/kcm_ksplashthemes.la
%{tde_prefix}/%{_lib}/trinity/kcm_ksplashthemes.so
%{tde_prefix}/%{_lib}/trinity/ksplashdefault.la
%{tde_prefix}/%{_lib}/trinity/ksplashdefault.so
%{tde_prefix}/%{_lib}/trinity/ksplashunified.la
%{tde_prefix}/%{_lib}/trinity/ksplashunified.so
%{tde_prefix}/%{_lib}/trinity/ksplashredmond.la
%{tde_prefix}/%{_lib}/trinity/ksplashredmond.so
%{tde_prefix}/%{_lib}/trinity/ksplashstandard.la
%{tde_prefix}/%{_lib}/trinity/ksplashstandard.so
%{tde_prefix}/%{_lib}/libksplashthemes.so.*
%{tde_prefix}/share/applications/tde/ksplashthememgr.desktop
%{tde_prefix}/share/apps/ksplash
%{tde_prefix}/share/services/ksplashdefault.desktop
%{tde_prefix}/share/services/ksplash.desktop
%{tde_prefix}/share/services/ksplashunified.desktop
%{tde_prefix}/share/services/ksplashredmond.desktop
%{tde_prefix}/share/services/ksplashstandard.desktop
%{tde_prefix}/share/servicetypes/ksplashplugins.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ksplashml/

##########

%package -n trinity-ksplash-devel
Summary:	Development files for ksplash
Group:		Development/Libraries/Other
Requires:	trinity-ksplash = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksplash-devel
This package contains the development files for ksplash.

%files -n trinity-ksplash-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/ksplash/
%{tde_prefix}/%{_lib}/libksplashthemes.la
%{tde_prefix}/%{_lib}/libksplashthemes.so

##########

%package -n trinity-ksysguard
Summary:	System guard for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ksysguardd = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksysguard
TDE System Guard allows you to monitor various statistics about your
computer.

%files -n trinity-ksysguard
%defattr(-,root,root,-)
%{tde_prefix}/bin/kpm
%{tde_prefix}/bin/ksysguard
%{tde_prefix}/%{_lib}/trinity/sysguard_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/sysguard_panelapplet.so
%{tde_prefix}/%{_lib}/libksgrd.so.*
%{tde_prefix}/share/applications/tde/ksysguard.desktop
%{tde_prefix}/share/apps/kicker/applets/ksysguardapplet.desktop
%{tde_prefix}/share/apps/ksysguard/
%{tde_prefix}/share/icons/crystalsvg/*/apps/ksysguard.png
%{tde_prefix}/share/mimelnk/application/x-ksysguard.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ksysguard/

##########

%package -n trinity-ksysguard-devel
Summary:	Development files for ksysguard
Group:		Development/Libraries/Other
Requires:	trinity-ksysguard = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksysguard-devel
This package contains the development files for ksysguard.

%files -n trinity-ksysguard-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/ksgrd/
%{tde_prefix}/%{_lib}/libksgrd.la
%{tde_prefix}/%{_lib}/libksgrd.so

##########

%package -n trinity-ksysguardd
Summary:	System guard daemon for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksysguardd
TDE System Guard Daemon is the daemon part of ksysguard. The daemon can
be installed on a remote machine to enable ksysguard on another machine
to monitor it through the daemon running there.

%files -n trinity-ksysguardd
%defattr(-,root,root,-)
%{tde_prefix}/bin/ksysguardd
%config(noreplace) %{_sysconfdir}/trinity/ksysguarddrc

##########

%package -n trinity-ktip
Summary:	Useful tips for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ktip
ktip provides many useful tips on using TDE when you log in.

%files -n trinity-ktip
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktip
%{tde_prefix}/share/applications/tde/ktip.desktop
%{tde_prefix}/share/applnk/Toys/ktip.desktop
%{tde_prefix}/share/apps/tdewizard/
%{tde_prefix}/share/autostart/ktip.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/ktip.*

##########

%package -n trinity-twin
Summary:	The TDE window manager
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-twin
This package contains the default X window manager for TDE.

%files -n trinity-twin
%defattr(-,root,root,-)
%{tde_prefix}/bin/twin
%{tde_prefix}/bin/twin_killer_helper
%{tde_prefix}/bin/twin_resumer_helper
%{tde_prefix}/bin/twin_rules_dialog
%{tde_prefix}/%{_lib}/tdeconf_update_bin/twin_update_default_rules
%{tde_prefix}/%{_lib}/tdeconf_update_bin/twin_update_window_settings
%{tde_prefix}/%{_lib}/trinity/kcm_twin*.la
%{tde_prefix}/%{_lib}/trinity/kcm_twin*.so
%{tde_prefix}/%{_lib}/trinity/twin*.la
%{tde_prefix}/%{_lib}/trinity/twin*.so
%{tde_prefix}/%{_lib}/libtdecorations.so.*
%{tde_prefix}/%{_lib}/libtdeinit_twin_rules_dialog.la
%{tde_prefix}/%{_lib}/libtdeinit_twin_rules_dialog.so
%{tde_prefix}/%{_lib}/libtdeinit_twin.la
%{tde_prefix}/%{_lib}/libtdeinit_twin.so
%{tde_prefix}/share/applications/tde/showdesktop.desktop
%{tde_prefix}/share/applications/tde/twindecoration.desktop
%{tde_prefix}/share/applications/tde/twinoptions.desktop
%{tde_prefix}/share/applications/tde/twinrules.desktop
%{tde_prefix}/share/applnk/.hidden/twinactions.desktop
%{tde_prefix}/share/applnk/.hidden/twinactiveborders.desktop
%{tde_prefix}/share/applnk/.hidden/twinadvanced.desktop
%{tde_prefix}/share/applnk/.hidden/twinfocus.desktop
%{tde_prefix}/share/applnk/.hidden/twinmoving.desktop
%{tde_prefix}/share/applnk/.hidden/twintranslucency.desktop
%{tde_prefix}/share/apps/tdeconf_update/twin3_plugin.pl
%{tde_prefix}/share/apps/tdeconf_update/twin3_plugin.upd
%{tde_prefix}/share/apps/tdeconf_update/twin_focus1.sh
%{tde_prefix}/share/apps/tdeconf_update/twin_focus1.upd
%{tde_prefix}/share/apps/tdeconf_update/twin_focus2.sh
%{tde_prefix}/share/apps/tdeconf_update/twin_focus2.upd
%{tde_prefix}/share/apps/tdeconf_update/twin_fsp_workarounds_1.upd
%{tde_prefix}/share/apps/tdeconf_update/twiniconify.upd
%{tde_prefix}/share/apps/tdeconf_update/twinsticky.upd
%{tde_prefix}/share/apps/tdeconf_update/twin.upd
%{tde_prefix}/share/apps/tdeconf_update/twinupdatewindowsettings.upd
%{tde_prefix}/share/apps/tdeconf_update/pluginlibFix.pl
%{tde_prefix}/share/apps/twin/
%{tde_prefix}/share/config.kcfg/twin.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/twin.png
%{tde_prefix}/share/doc/tde/HTML/en/kompmgr/

##########

%package -n trinity-twin-devel
Summary:	Development files for twin
Group:		Development/Libraries/Other
Requires:	trinity-twin = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-twin-devel
This package contains the development files for twin.

%files -n trinity-twin-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/twin/
%{tde_prefix}/include/tde/kcommondecoration.h
%{tde_prefix}/include/tde/kdecoration.h
%{tde_prefix}/include/tde/kdecoration_p.h
%{tde_prefix}/include/tde/kdecoration_plugins_p.h
%{tde_prefix}/include/tde/kdecorationfactory.h
%{tde_prefix}/include/tde/KWinInterface.h
%{tde_prefix}/%{_lib}/libtdecorations.la
%{tde_prefix}/%{_lib}/libtdecorations.so

##########

%package -n trinity-libkonq
Summary:	Core libraries for Konqueror
Group:		System/GUI/Other

%description -n trinity-libkonq
These libraries are used by several TDE applications, most notably
Konqueror and the kdesktop package.

%files -n trinity-libkonq
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kded_favicons.la
%{tde_prefix}/%{_lib}/trinity/kded_favicons.so
%{tde_prefix}/%{_lib}/trinity/konq_sound.la
%{tde_prefix}/%{_lib}/trinity/konq_sound.so
%{tde_prefix}/%{_lib}/libkonq.so.*
%{tde_prefix}/share/apps/kbookmark/
%{tde_prefix}/share/apps/tdeconf_update/favicons.upd
%{tde_prefix}/share/apps/tdeconf_update/move_favicons.sh
%dir %{tde_prefix}/share/apps/konqueror/pics
%{tde_prefix}/share/apps/konqueror/pics/arrow_bottomleft.png
%{tde_prefix}/share/apps/konqueror/pics/arrow_bottomright.png
%{tde_prefix}/share/apps/konqueror/pics/arrow_topleft.png
%{tde_prefix}/share/apps/konqueror/pics/arrow_topright.png
%{tde_prefix}/share/apps/konqueror/pics/thumbnailfont_7x4.png
%{tde_prefix}/share/services/kded/favicons.desktop
%{tde_prefix}/share/servicetypes/konqpopupmenuplugin.desktop

##########

%package libtqt3-integration
Summary:	Integration library between TQt3 and TDE
Group:		System/GUI/Other

Obsoletes:	tdebase-libtqt3-integration < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-libtqt3-integration = %{?epoch:%{epoch}:}%{version}-%{release}

%description libtqt3-integration
These libraries allow you to use TDE dialogs in native TQt3 applications.

%files libtqt3-integration
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/integration/
%{tde_prefix}/%{_lib}/trinity/kded_tdeintegration.la
%{tde_prefix}/%{_lib}/trinity/kded_tdeintegration.so
%{tde_prefix}/share/services/kded/tdeintegration.desktop

##########

%package -n trinity-libkonq-devel
Summary:	Development files for Konqueror's core libraries
Group:		Development/Libraries/Other
Requires:	trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

%description -n trinity-libkonq-devel
This package contains headers and other development files for the core
Konqueror libraries.

%files -n trinity-libkonq-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/tdefileivi.h
%{tde_prefix}/include/tde/kivdirectoryoverlay.h
%{tde_prefix}/include/tde/kivfreespaceoverlay.h
%{tde_prefix}/include/tde/knewmenu.h
%{tde_prefix}/include/tde/konqbookmarkmanager.h
%{tde_prefix}/include/tde/konq_*.h
%{tde_prefix}/include/tde/libkonq_export.h
%{tde_prefix}/%{_lib}/libkonq.la
%{tde_prefix}/%{_lib}/libkonq.so

##########

%package tdeio-smb-plugin
Summary:	Windows Connection Module for TDE
Group:		System/GUI/Other

%description tdeio-smb-plugin
This package provides the "smb://" protocol, to connect to and from
Windows and Samba shares.

%files tdeio-smb-plugin
%defattr(-,root,root)
%{tde_prefix}/%{_lib}/trinity/kcm_samba.la
%{tde_prefix}/%{_lib}/trinity/kcm_samba.so
%{tde_prefix}/%{_lib}/trinity/tdeio_smb.la
%{tde_prefix}/%{_lib}/trinity/tdeio_smb.so
%{tde_prefix}/share/services/smb.protocol
%{tde_prefix}/share/apps/konqueror/dirtree/remote/smb-network.desktop
%dir %{tde_prefix}/share/apps/remoteview
%{tde_prefix}/share/apps/remoteview/smb-network.desktop
%{tde_prefix}/share/mimelnk/application/x-smb-workgroup.desktop

%prep -a
# Applies an optional distro-specific graphical theme
%if "%{?tde_bg}" != ""
# TDM Background
%__sed -i "tdm/kfrontend/gentdmconf.c" \
	-e 's|"Wallpaper=isadora.png\n"|"Wallpaper=%{tde_bg}\n"|'

# TDE user default background
%__sed -i "kpersonalizer/keyecandypage.cpp" \
	-e 's|#define DEFAULT_WALLPAPER "isadora.png"|#define DEFAULT_WALLPAPER "%{tde_bg}"|'
%__sed -i "starttde" \
	-e 's|%{tde_prefix}/share/wallpapers/Trinity-lineart.svg.desktop|%{tde_bg}|' \
	-e 's|Wallpaper=Trinity-lineart.svg|Wallpaper=%{tde_bg}|'
%endif

# TDE default directory and icon in startup script
%__sed -i "starttde" \
	-e "s|/opt/trinity|%{tde_prefix}|g"

# Sets default TDE menu icon
%if "%{tde_starticon}" != ""
%__sed -i "kicker/libkicker/kickerSettings.kcfg" \
	-e "s|QString(\"kmenu\")|QString(\"%{tde_starticon}\")|"
%endif


# Reboot command location may vary on some distributions
if [ -x "/usr/bin/reboot" ]; then
  POWEROFF="/usr/bin/poweroff"
  REBOOT="/usr/bin/reboot"
elif [ -x "/usr/sbin/reboot" ]; then
  POWEROFF="/usr/sbin/poweroff"
  REBOOT="/usr/sbin/reboot"
fi
if [ -n "${REBOOT}" ]; then
  %__sed -i \
    "doc/tdm/tdmrc-ref.docbook" \
    "kcontrol/tdm/tdm-shut.cpp" \
    "tdm/config.def" \
  -e "s|/sbin/poweroff|${POWEROFF}|g" \
  -e "s|/sbin/reboot|${REBOOT}|g"
fi

# Update icons for some control center modules
%__sed -i "kcontrol/componentchooser/componentchooser.desktop"        -e "s|^Icon=.*|Icon=kcmcomponentchooser|"
%__sed -i "kcontrol/taskbar/kcmtaskbar.desktop"                       -e "s|^Icon=.*|Icon=kcmtaskbar|"
%__sed -i "kcontrol/nics/nic.desktop"                                 -e "s|^Icon=.*|Icon=kcmnic|"
%__sed -i "kcontrol/input/mouse.desktop"                              -e "s|^Icon=.*|Icon=kcmmouse|"
%__sed -i "kcontrol/smserver/kcmsmserver.desktop"                     -e "s|^Icon=.*|Icon=kcmsmserver|"
%__sed -i "kcontrol/kded/kcmkded.desktop"                             -e "s|^Icon=.*|Icon=kcmkded|"
%__sed -i "kcontrol/konq/desktop.desktop"                             -e "s|^Icon=.*|Icon=kcmdesktop|"
%__sed -i "kcontrol/konq/desktopbehavior.desktop"                     -e "s|^Icon=.*|Icon=kcmdesktopbehavior|"
%__sed -i "kcontrol/privacy/privacy.desktop"                          -e "s|^Icon=.*|Icon=kcmprivacy|"
%__sed -i "kcontrol/crypto/crypto.desktop"                            -e "s|^Icon=.*|Icon=kcmcrypto|"
%__sed -i "kcontrol/tdeio/netpref.desktop"                            -e "s|^Icon=.*|Icon=kcmnetpref|"
%__sed -i "kcontrol/konqhtml/tdehtml_filter.desktop"                  -e "s|^Icon=.*|Icon=kcmkhtml_filter|"
%__sed -i "kcontrol/joystick/joystick.desktop"                        -e "s|^Icon=.*|Icon=kcmjoystick|"
%__sed -i "kcontrol/colors/colors.desktop"                            -e "s|^Icon=.*|Icon=kcmcolors|"
%__sed -i "kcontrol/performance/kcmperformance.desktop"               -e "s|^Icon=.*|Icon=kcmperformance|"
%__sed -i "kcontrol/launch/kcmlaunch.desktop"                         -e "s|^Icon=.*|Icon=kcmlaunch|"
%__sed -i "kcontrol/dnssd/kcm_tdednssd.desktop"                       -e "s|^Icon=.*|Icon=kcmkdnssd|"
%__sed -i "kcontrol/spellchecking/spellchecking.desktop"              -e "s|^Icon=.*|Icon=kcmspellchecking|"
%__sed -i "konqueror/sidebar/trees/history_module/kcmhistory.desktop" -e "s|^Icon=.*|Icon=kcmhistory|"
%__sed -i "tdeioslave/cgi/kcmcgi/kcmcgi.desktop"                      -e "s|^Icon=.*|Icon=kcmcgi|"
%__sed -i "tdeioslave/media/tdecmodule/media.desktop"                 -e "s|^Icon=.*|Icon=kcmmedia|" 


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"

%install -p
# Symlinks 'usb.ids' (Use system-provided version, not TDE provided version)
%__mkdir_p %{?buildroot}%{tde_prefix}/share/apps/
%__ln_s -f "/usr/share/hwdata/usb.ids" "%{?buildroot}%{tde_prefix}/share/apps/usb.ids"

# Console font to fontconfig
%__mkdir_p "%{buildroot}%{_sysconfdir}/fonts/conf.d"
cat <<EOF >"%{buildroot}%{_sysconfdir}/fonts/conf.d/99-konsole.conf"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <!-- Font directory list -->
  <dir>%{tde_prefix}/share/apps/konsole/fonts</dir>
</fontconfig>
EOF

# logrotate configuration
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat << EOF > "%{buildroot}%{_sysconfdir}/logrotate.d/trinity-tdm"
/var/log/tdm.log {
    weekly
    notifempty
    missingok
    nocompress
}
EOF

# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p "%{?buildroot}%{tde_prefix}/share/icons/hicolor/"{16x16,22x22,32x32,48x48,64x64,128x128}"/apps/"
pushd "%{?buildroot}%{tde_prefix}/share/icons"
for i in {16,32,48,64,128};    do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/mimetypes/application-vnd.tde.misc.png  hicolor/"$i"x"$i"/apps/kcmcomponentchooser.png  ;done
for i in {16,22,32,48,128};    do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/launch.png                      hicolor/"$i"x"$i"/apps/kcmperformance.png       ;done
for i in 16;                   do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/services.png                    hicolor/"$i"x"$i"/apps/kcmkded.png              ;done
for i in {16,22,32,48};        do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/system-log-out.png              hicolor/"$i"x"$i"/apps/kcmsmserver.png          ;done
for i in {16,22,32};           do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/tools-check-spelling.png        hicolor/"$i"x"$i"/apps/kcmspellchecking.png     ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/places/desktop.png                      hicolor/"$i"x"$i"/apps/kcmdesktopbehavior.png   ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/places/desktop.png                      hicolor/"$i"x"$i"/apps/kcmdesktop.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/kmenu.png                          hicolor/"$i"x"$i"/apps/kcmtaskbar.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/mimetypes/application-x-kcsrc.png       hicolor/"$i"x"$i"/apps/kcmcolors.png            ;done
for i in {16,22,32,48,128};    do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/launch.png                      hicolor/"$i"x"$i"/apps/kcmlaunch.png            ;done
for i in {16,22,32};           do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/filter.png                      hicolor/"$i"x"$i"/apps/kcmkhtml_filter.png      ;done
for i in {16,22,32};           do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/system-run.png                  hicolor/"$i"x"$i"/apps/kcmcgi.png               ;done
for i in {16,22};              do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/history.png                     hicolor/"$i"x"$i"/apps/kcmhistory.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/places/network.png                      hicolor/"$i"x"$i"/apps/kcmnetpref.png           ;done
for i in {16,32,48,64,128};    do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/blockdevice.png                 hicolor/"$i"x"$i"/apps/kcmkdnssd.png            ;done
for i in {16,22,32,48,64};     do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/input-joystick.png              hicolor/"$i"x"$i"/apps/kcmjoystick.png          ;done
for i in {16,32,48,64,128};    do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/input-mouse.png                 hicolor/"$i"x"$i"/apps/kcmmouse.png             ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/computer.png                    hicolor/"$i"x"$i"/apps/kcmmedia.png             ;done
for i in {16,22,32};           do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/encrypted.png                   hicolor/"$i"x"$i"/apps/kcmcrypto.png            ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/places/trashcan_empty.png               hicolor/"$i"x"$i"/apps/kcmprivacy.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/places/network.png                      hicolor/"$i"x"$i"/apps/kcmnic.png               ;done
popd

# PAM configuration files (except openSUSE)
%__install -D -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pam.d/tdm-trinity"
%__install -D -m 644 "%{SOURCE3}" "%{?buildroot}%{_sysconfdir}/pam.d/tdm-trinity-np"
%__install -D -m 644 "%{SOURCE4}" "%{?buildroot}%{_sysconfdir}/pam.d/kcheckpass-trinity"
%__install -D -m 644 "%{SOURCE5}" "%{?buildroot}%{_sysconfdir}/pam.d/tdescreensaver-trinity"

%install -a
# Makes 'media_safelyremove.desktop' an alternative.
# This allows the use of 'tdeio-umountwrapper' package.
%__mv -f "%{buildroot}%{tde_prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop" "%{buildroot}%{tde_prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase"
%__mkdir_p "%{buildroot}%{_sysconfdir}/alternatives"

# Adds a GDM/KDM/XDM session called 'TDE'
%__install -D -m 644 \
	"%{?buildroot}%{tde_prefix}/share/apps/tdm/sessions/tde.desktop" \
	"%{?buildroot}%{_datadir}/xsessions/tde.desktop"

# Move faces icon to XDG directory '/usr/share/faces'
if [ ! -d "%{?buildroot}%{_datadir}/faces" ]; then
  %__mkdir_p "%{?buildroot}%{_datadir}/faces"
  %__mv -f "%{?buildroot}%{tde_prefix}/share/apps/tdm/pics/users/"* "%{?buildroot}%{_datadir}/faces" 2>/dev/null
  rmdir "%{?buildroot}%{tde_prefix}/share/apps/tdm/pics/users"
fi
%__ln_s "%{_datadir}/faces" "%{?buildroot}%{tde_prefix}/share/apps/tdm/pics/users"

%__install -d -m 755 %{?buildroot}%{_sysconfdir}/X11/wmsession.d
cat <<EOF >"%{?buildroot}%{_sysconfdir}/X11/wmsession.d/45TDE"
NAME=TDE
ICON=kde-wmsession.xpm
DESC=The Trinity Desktop Environment
EXEC=%{tde_prefix}/bin/starttde
SCRIPT:
exec %{tde_prefix}/bin/starttde
EOF

%__install -d -m 755 %{?buildroot}%{_datadir}/X11/dm.d
cat <<EOF >"%{?buildroot}%{_datadir}/X11/dm.d/45TDE.conf"
NAME=TDM
DESCRIPTION=TDM (Trinity Display Manager)
PACKAGE=trinity-tdm
EXEC=%{tde_prefix}/bin/tdm
EOF

# TDM configuration
%__sed -i "s/^#*MinShowUID=.*\b/MinShowUID=1000/" "%{buildroot}%{_sysconfdir}/trinity/tdm/tdmrc"

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{tde_prefix}/share/applications/tde/*.desktop ; do
  if grep -q "^Categories=.*X-TDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=TDE" "${i}" ; then
      echo "OnlyShowIn=TDE;" >>"${i}"
    fi
  fi
done

# Other apps that should stay in TDE
for i in ksysguard tde-kcontrol tdefontview showdesktop; do
  echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/${i}.desktop"
done

# Remove setuid bit on some binaries.
%{?with_tsak:chmod 0511 "%{?buildroot}%{tde_prefix}/bin/tdmtsak"}
chmod 0755 "%{?buildroot}%{tde_prefix}/bin/kcheckpass"
%{?with_kbdledsync:chmod 0755 "%{?buildroot}%{tde_prefix}/bin/tdekbdledsync"}

# Fix permissions on shell scripts
chmod 0755 "%{?buildroot}%{tde_prefix}/share/apps/tdeconf_update/move_session_config.sh"
chmod 0755 "%{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/khelpcenter/glossary/checkxrefs"

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

# fix desktop icon names per XDG spec
mv %{?buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/My_Computer %{buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/My_Computer.desktop
mv %{?buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/My_Documents %{buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/My_Documents.desktop
mv %{?buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/My_Network_Places %{buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/My_Network_Places.desktop
mv %{?buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/Printers %{buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/Printers.desktop
mv %{?buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/Trash %{buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/Trash.desktop
mv %{?buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/Web_Browser %{buildroot}/%{tde_prefix}/share/apps/kdesktop/Desktop/Web_Browser.desktop

# Removes obsolete Beagle-related files
%__rm -f %{?buildroot}%{tde_prefix}/bin/khc_beagle_index.pl
%__rm -f %{?buildroot}%{tde_prefix}/bin/khc_beagle_search.pl

# Remove conflicting doc
%__rm -rf "%{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/gopher"

# Removes tderandrtray documentation, if not built.
%{!?with_tderandrtray:%__rm -rf "%{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/tderandrtray"}

