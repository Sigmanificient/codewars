function maskify(cc) {
    /*
    * Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most
    *  secret question is still correct. However, since someone could look over your shoulder, you don't want that shown
    * on your screen. Instead, we mask it.
    *
    * Your task is to write a function maskify, which changes all but the last four characters into '#'.
    *  */
  let len = cc.length;

  if (len <= 4) {
    return cc;
  }

  return "#".repeat(len - 4) + cc.substring(len - 4);
}
