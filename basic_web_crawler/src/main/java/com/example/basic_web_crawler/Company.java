package com.example.basic_web_crawler;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(value = { "desc" })
public class Company {
    private String logo;
    private String desc;

    public Company(){}
    public Company(String logo, String desc) {
        this.logo = logo;
        this.desc = desc;
    }

    public String getLogo() {
        return logo;
    }

    public void setImg(String logo) {
        this.logo = logo;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

}
