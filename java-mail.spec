Summary: 	JavaMail
Name:		javamail
Version:	1.2
Release:	1
License:	Read LICENSE.txt!
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	javamail-1_2.zip
URL:		http://java.sun.com/products/javamail
Requires:	jaf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
javamail

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	JavaMail documentation

%description doc
JavaMail documentation

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp *.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf CHANGES.txt LICENSE.txt NOTES.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc demo docs
