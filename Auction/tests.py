from django.test import TestCase
from .models import Category, Comment, User, Listing, Bid

class AuctionTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user('homayoon', password='1991')
        self.user_2 = User.objects.create_user('nooshin', password='1991')
        self.listing_1 = Listing.objects.create(title='listing_1',
                                description='desc',
                                user=self.user_1,
                                starting_price=1000)
        self.category_1 = Category.objects.create(name='category_1')
        self.listing_1.category.add(self.category_1)
        self.listing_1.watchers.add(self.user_2)
        self.bid_1 = Bid.objects.create(user= self.user_2,
                                        amount=1200)
        self.listing_1.current_bid = self.bid_1
        self.comment_1 = Comment.objects.create(user = self.user_1,
                                                content = 'comment_1',
                                                listing = self.listing_1)
        

    def test_user_password(self):
        checked = self.user_1.check_password('1991')
        self.assertTrue(checked)    

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_listing_count(self):
        qs = Listing.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_listing_properties(self):
        asserts = [
            self.listing_1.title =='listing_1',
            self.listing_1.description == 'desc',
            self.listing_1.user == self.user_1,
            self.listing_1.starting_price == 1000,
            self.listing_1.current_bid == self.bid_1,
            self.listing_1.is_active == True,
            self.listing_1.watchers.all().count() == 1,
            self.listing_1.category.all().count() == 1,
        ]
        self.assertTrue(all(asserts))

    def test_bid_properties(self):
        asserts = [
            self.bid_1.user == self.user_2,
            self.bid_1.amount == 1200,
        ]
        self.assertTrue(all(asserts))

    def test_comment_properties(self):
        asserts = [
            self.comment_1.user == self.user_1,
            self.comment_1.content == 'comment_1',
            self.comment_1.listing == self.listing_1,
        ]
        self.assertTrue(all(asserts))

    def test_user_wachlist_count(self):
        qs = self.user_2.watchlist.all()
        self.assertEqual(qs.count(), 1)

    def test_bid_count(self):
        qs = Bid.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_listing_reverse_count(self):
        qs = self.user_1.listings.all()
        self.assertEqual(qs.count(), 1)

    def test_category_count(self):
        qs = self.listing_1.category.all()
        self.assertEqual(qs.count(), 1)
    
    def test_category_reverse_count(self):
        qs = self.category_1.listings.all()
        self.assertEqual(qs.count(), 1)

    def test_comment_count(self):
        qs = Comment.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_listing_comments_count(self):
        qs = self.listing_1.comments.all()
        self.assertEqual(qs.count(), 1)

    

    
    






