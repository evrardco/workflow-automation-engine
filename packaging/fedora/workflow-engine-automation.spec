Name:           workflow-automation-engine
Version:        beta
Release:        1%{?dist}
Summary:        Workflow automation engine

License:        AGPLv3
URL:            https://github.com/HugoCornelis/workflow-automation-engine
Source0:        https://github.com/HugoCornelis/workflow-automation-engine/archive/refs/heads/master.zip

BuildRequires:  perl-Expect perl-File-chdir perl-File-Find-Rule perl-Inline-Python perl-JSON perl-Net-IP perl-TOML-Parser perl-YAML perl-XML-Parser grc automake
Requires:       perl-Expect perl-File-chdir perl-File-Find-Rule perl-Inline-Python perl-JSON perl-Net-IP perl-TOML-Parser perl-YAML perl-XML-Parser grc automake

%description
Main binary for the workflow automation engine, allowing to create, install and use workflow configurations

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Tue Feb 03 2026 Super User
- 
