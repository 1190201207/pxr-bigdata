

#include <memory>
#include <vector>

#include "helper.h"
#include "xindex_root.h"
#include "xindex_util.h"

#if !defined(XINDEX_H)
#define XINDEX_H

namespace xindex {

template <class key_t, class val_t>
class XIndex {
  typedef HRoot<key_t, val_t> root_t;

 public:
  XIndex(const std::vector<key_t> &keys, const std::vector<val_t> &vals,
         size_t worker_num, size_t bg_n);
  ~XIndex();

  inline bool get(const key_t &key, val_t &val, const uint32_t worker_id);
  inline bool put(const key_t &key, const val_t &val, const uint32_t worker_id);
  inline bool remove(const key_t &key, const uint32_t worker_id);

 private:
  void start_bg();
  void terminate_bg();
  static void *background(void *this_);

  root_t *volatile root = nullptr;
  pthread_t bg_master;
  size_t bg_num;
  volatile bool bg_running = true;
};

}  // namespace xindex

#endif  // XINDEX_H
