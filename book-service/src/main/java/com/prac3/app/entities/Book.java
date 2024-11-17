package com.prac3.app.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity 
public class Book {
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO) 
	private int bookId; 
	private String title; 
	private String author; 
	private String isbn; 
	private String description; 
	private String publisher; 
	private String publishedDate; 
	private Float price;
	
}
