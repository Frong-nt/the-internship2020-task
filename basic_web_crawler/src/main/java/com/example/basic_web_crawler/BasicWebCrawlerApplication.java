package com.example.basic_web_crawler;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

@SpringBootApplication
@RestController
public class BasicWebCrawlerApplication {
    private static ArrayList<Company>  companies = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        SpringApplication.run(BasicWebCrawlerApplication.class, args);
        String url = "https://theinternship.io//";
        Document document = Jsoup.connect(url).get();
        Elements companiesDom = document.select("#__layout > div > div > section:nth-child(5) > div > div.columns.is-multiline > div");

        for (Element companyDom: companiesDom){
            companies.add(new Company(companyDom.select("img[src]").attr("src"), companyDom.text()));
        }
        companyDesSort(companies);
        for(Company company: companies){
            System.out.println(company.getLogo());
        }

    }
    @RequestMapping(value = "/companies", method = RequestMethod.GET)
    public  HashMap<String, ArrayList<Company>> getCompanies(){
        HashMap<String, ArrayList<Company>> map = new HashMap<>();
        map.put("companies", companies);
        return map;
    }

//    sort length of description each company
    public static void companyDesSort(ArrayList<Company> companies){
          while (true){
              boolean status = false;
              for(int index=0;index< companies.size()-1;index++){
                  Company temp, temp2;
                  if(companies.get(index+1).getDesc().length()< companies.get(index+1).getDesc().length()){
                      temp = companies.get(index);
                      temp2 = companies.get(index+1);
                      companies.set(index, temp2);
                      companies.set(index+1, temp);
                      status = true;
                  }
              }
              if(!status)
                  break;
          }
    }

}
