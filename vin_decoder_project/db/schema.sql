CREATE TABLE wmi_data (
    wmi VARCHAR(3) PRIMARY KEY,
    manufacturer VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE vds_data (
    wmi VARCHAR(3),
    vds VARCHAR(5),
    model VARCHAR(100),
    engine VARCHAR(100),
    body_style VARCHAR(100),
    PRIMARY KEY (wmi, vds)
);

CREATE TABLE year_codes (
    code CHAR(1) PRIMARY KEY,
    year INT
);