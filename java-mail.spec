Summary:	JavaMail - Java mail system
Summary(pl.UTF-8):   JavaMail - system pocztowy w Javie
Name:		javamail
Version:	1.4
Release:	1
License:	restricted, non-distributable (Sun Binary Code License - see LICENSE.txt)
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/javamail/downloads/
Source0:	%{name}-%(echo %{version} | tr . _).zip
# NoSource0-md5:	4541a84c4d329291fe87b57fde276b0e
NoSource:	0
URL:		http://java.sun.com/products/javamail/
BuildRequires:	unzip
Requires:	jaf
Requires:	jre >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The JavaMail(TM) API provides a set of abstract classes that model a
mail system. The API provides a platform independent and protocol
independent framework to build Java technology-based mail and
messaging applications.

%description -l pl.UTF-8
API JavaMail(TM) daje zestaw klas abstrakcyjnych tworzących system
pocztowy. API daje niezależne od platformy i protokołu środowisko do
tworzenia aplikacji pocztowych i komunikacyjnych w oparciu o Javę.

%package doc
Summary:	JavaMail documentation
Summary(pl.UTF-8):   Dokumentacja do JavaMail
Group:		Development/Languages/Java

%description doc
JavaMail documentation.

%description doc -l pl.UTF-8
Dokumentacja do JavaMail.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
install *.jar $RPM_BUILD_ROOT%{_javalibdir}
install lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt NOTES.txt README.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc demo docs
