package com.example.springtemplate.models;

import javax.persistence.*;

@Entity
@Table(name="users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String first_name; // first_name
    private String last_name;
    private String username;
    private String password;
    private String address;
    private Integer zip;
    private long phone_number;
    private String email;
    private Integer account_type;

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public String getFirstName() { return first_name; }
    public void setFirstName(String first_name) { this.first_name = first_name; }

    public String getLastName() { return last_name; }
    public void setLastName(String last_name) { this.last_name = last_name; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }

    public String getAddress() { return address; }
    public void setAddress(String address) {this.address = address;}

    public Integer getZip() { return zip; }
    public void setZip(Integer zip) { this.zip = zip; }

    public long getPhoneNumber() { return phone_number; }
    public void setPhoneNumber(long phone_number) { this.phone_number = phone_number; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public Integer getAccountType() { return account_type; }
    public void setAccountType(Integer account_type) { this.account_type = account_type; }

    public User(String first_name, String last_name, String username, String password, String address, Integer zip, long phone_number, String email, Integer account_type){
        this.first_name = first_name;
        this.last_name = last_name;
        this.username = username;
        this.password = password;
        this.address = address;
        this.zip = zip;
        this.phone_number = phone_number;
        this.email = email;
        this.account_type = account_type;
    }

    public User() {}
}
