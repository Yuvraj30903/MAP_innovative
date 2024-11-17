package com.prac3.app.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.prac3.app.entities.Book;
import com.prac3.app.services.BookService;
 
@RestController
@CrossOrigin("*")
@RequestMapping("/api/book")
public class BookController {

	@Autowired
	private BookService bookService;
	@PostMapping(path = "/",consumes = "application/json")
	public ResponseEntity<Book> createBook(@RequestBody Book book )
	{
		try {
			System.out.println(book);
			Book tmp=bookService.createBook(book);
			return ResponseEntity.status(HttpStatus.OK).body(tmp);
		} catch (Exception e) {
			return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
		}
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<Book> getBooks(@PathVariable("id") Long bookId)
	{
		try { 
			Book tmp=bookService.getBook(bookId);
			return ResponseEntity.status(HttpStatus.OK).body(tmp);
		} catch (Exception e) {
			return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
		}
	}
	@GetMapping("/")
	public ResponseEntity<List<Book>> getAllBooks()
	{
		try { 
			List<Book> tmp=bookService.getAllBook();
			return ResponseEntity.status(HttpStatus.OK).body(tmp);
		} catch (Exception e) {
			return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
		}
	}
	@DeleteMapping("/{id}")
	public ResponseEntity<Boolean> deleteBook(@PathVariable("id") Long bookId)
	{
		try { 
			boolean del=bookService.deleteBook(bookId);
			return ResponseEntity.status(HttpStatus.OK).body(true);
		} catch (Exception e) {
			return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
		}
	}
	@PutMapping("/")
	public ResponseEntity<Book> deleteBook(@RequestBody Book book)
	{
		try { 
			book=bookService.updateBook(book);
			return ResponseEntity.status(HttpStatus.OK).body(book);
		} catch (Exception e) {
			return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
		}
	}
}
