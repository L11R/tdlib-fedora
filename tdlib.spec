Name:           tdlib
Version:        master
Release:        1%{?dist}
Summary:        Cross-platform library for building Telegram clients

License:        BSL-1.0
URL:            https://github.com/tdlib/td
Source0:        https://github.com/tdlib/td/archive/%{version}.zip

BuildRequires:  cmake,gperf,openssl-devel

%description

%prep
%setup -n td-%{version}

%build
mkdir build
cd build
%cmake -DCMAKE_BUILD_TYPE=Release ..
%make_build

%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install

%files
%{_includedir}/%{name}
%exclude /usr/lib/cmake/Td
%exclude /usr/lib/debug/usr/lib/libtdclient.so-master-1.fc28.x86_64.debug
%exclude /usr/lib/debug/usr/lib/libtdjson.so-master-1.fc28.x86_64.debug
/usr/lib/libtdactor.a
/usr/lib/libtdclient.so
/usr/lib/libtdcore.a
/usr/lib/libtddb.a
/usr/lib/libtdjson.so
/usr/lib/libtdjson_private.a
/usr/lib/libtdjson_static.a
/usr/lib/libtdnet.a
/usr/lib/libtdsqlite.a
/usr/lib/libtdutils.a

%changelog
* Fri Sep 14 2018 L11R <savely@krasovsky.me>
- Initial release
- Minor fixes
