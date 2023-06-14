#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: The head of the singly linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/* Find the middle node using slow and fast pointers */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	/* Handle odd-length list by moving slow to the next node */
	if (fast != NULL)
	{
		prev = slow;
		slow = slow->next;
	}
	/* Reverse the second half of the list */
	prev->next = NULL;
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	/* Check if the reversed second half matches the first half */
	slow = prev; /* slow points to the head of the reversed second half */
	fast = *head; /* fast points to the head of the first half */
	while (slow != NULL && fast != NULL)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
