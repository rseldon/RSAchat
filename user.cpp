#include "user.h"

class user 
{
	public:
		unsigned long long get_publicKey();
		unsigned long long get_modulus();

	private:
		unsigned long long privateKey;
		unsigned long long publicKey;
		unsigned long long modulus;
};



user::user()
{
	assignKeys();
}

user::user(unsigned long privKey, unsigned long pubKey, unsigned long mod)
{
	privateKey = privKey;
	publicKey = pubKey;
	modulus = mod;
}


user::~user()
{
}
