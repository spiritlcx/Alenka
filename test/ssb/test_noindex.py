import shutil
import os
import pytest
import subprocess

@pytest.mark.incremental
class TestSSBNoIndex:

	def test_check_testdir(self, testdir):
		#clean up test dir
		for the_file in os.listdir(str(testdir.realpath())):
			file_path = os.path.join(str(testdir.realpath()), the_file)
			if os.path.isfile(file_path):
				os.unlink(file_path)

	def test_alenka(self, testdir):
		if not os.path.exists("../src/alenka"):
			raise Exception('missing src/alenka') 

		shutil.copy2("../src/alenka", str(testdir.realpath()))

	def test_cp_load(self, testdir):
		shutil.copy2("ssb/load/load_customer.sql", str(testdir.realpath()))
		shutil.copy2("ssb/load/load_date.sql", str(testdir.realpath()))
		shutil.copy2("ssb/load/load_lineorder.sql", str(testdir.realpath()))
		shutil.copy2("ssb/load/load_part.sql", str(testdir.realpath()))
		shutil.copy2("ssb/load/load_supplier.sql", str(testdir.realpath()))

	def test_cp_data(self, testdir):
		shutil.copy2("ssb/data/customer.tbl", str(testdir.realpath()))
		shutil.copy2("ssb/data/date.tbl", str(testdir.realpath()))
		shutil.copy2("ssb/data/lineorder.tbl", str(testdir.realpath()))
		shutil.copy2("ssb/data/part.tbl", str(testdir.realpath()))
		shutil.copy2("ssb/data/supplier.tbl", str(testdir.realpath()))

	def test_cp_query(self, testdir):
		shutil.copy2("ssb/query/noindex/ss11.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss12.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss13.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss21.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss22.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss23.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss31.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss32.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss33.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss34.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss41.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss42.sql", str(testdir.realpath()))
		shutil.copy2("ssb/query/noindex/ss43.sql", str(testdir.realpath()))

	def test_cp_result(self, testdir):
		shutil.copy2("ssb/result/ss11.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss12.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss13.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss21.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss22.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss23.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss31.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss32.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss33.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss34.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss41.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss42.result.txt", str(testdir.realpath()))
		shutil.copy2("ssb/result/ss43.result.txt", str(testdir.realpath()))

	def test_chdir(self, testdir):
		os.chdir(str(testdir.realpath()))

	def test_load_ssb_customer(self):
		if subprocess.call(["alenka", "load_customer.sql"]) != 0:
			raise Exception('load error')

	def test_load_ssb_date(self):
		if subprocess.call(["alenka", "load_date.sql"]) != 0:
			raise Exception('load error')

	def test_load_ssb_lineorder(self):
		if subprocess.call(["alenka", "load_lineorder.sql"]) != 0:
			raise Exception('load error')

	def test_load_ssb_part(self):
		if subprocess.call(["alenka", "load_part.sql"]) != 0:
			raise Exception('load error')

	def test_load_ssb_supplier(self):
		if subprocess.call(["alenka", "load_supplier.sql"]) != 0:
			raise Exception('load error')

	def test_query_ss11(self):
		if subprocess.call(["alenka", "ss11.sql"]) != 0:
			raise Exception('query error')
	
		r1 = open('ss11.result.txt', 'r')
		r2 = open('ss11.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()
		
	def test_query_ss12(self):
		if subprocess.call(["alenka", "ss12.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss12.result.txt', 'r')
		r2 = open('ss12.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss13(self):
		if subprocess.call(["alenka", "ss13.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss13.result.txt', 'r')
		r2 = open('ss13.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss21(self):
		if subprocess.call(["alenka", "ss21.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss21.result.txt', 'r')
		r2 = open('ss21.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss22(self):
		if subprocess.call(["alenka", "ss22.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss22.result.txt', 'r')
		r2 = open('ss22.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss23(self):
		if subprocess.call(["alenka", "ss23.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss23.result.txt', 'r')
		r2 = open('ss23.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss31(self):
		if subprocess.call(["alenka", "ss31.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss31.result.txt', 'r')
		r2 = open('ss31.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss32(self,):
		if subprocess.call(["alenka", "ss32.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss32.result.txt', 'r')
		r2 = open('ss32.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss33(self):
		if subprocess.call(["alenka", "ss33.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss33.result.txt', 'r')
		r2 = open('ss33.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss34(self):
		if subprocess.call(["alenka", "ss34.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss34.result.txt', 'r')
		r2 = open('ss34.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss41(self):
		if subprocess.call(["alenka", "ss41.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss41.result.txt', 'r')
		r2 = open('ss41.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss42(self):
		if subprocess.call(["alenka", "ss42.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss42.result.txt', 'r')
		r2 = open('ss42.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()

	def test_query_ss43(self):
		if subprocess.call(["alenka", "ss43.sql"]) != 0:
			raise Exception('query error')

		r1 = open('ss43.result.txt', 'r')
		r2 = open('ss43.txt', 'r')
		diff = difflib.SequenceMatcher(None, r1.read(), r2.read())
		if diff.ratio != 1.0:
			raise Exception('query results dont match!')

		r1.close()
		r2.close()
