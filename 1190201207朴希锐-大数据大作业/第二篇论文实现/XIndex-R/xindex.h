

#include "helper.h"
#include "xindex_buffer.h"
#include "xindex_group.h"
#include "xindex_model.h"
#include "xindex_root.h"
#include "xindex_util.h"

#if !defined(XINDEX_H)
#define XINDEX_H

namespace xindex {

template <class key_t, class val_t, bool seq = false>
class XIndex {
  typedef Group<key_t, val_t, seq> group_t;
  typedef Root<key_t, val_t, seq> root_t;
  typedef void iterator_t;

 public:
  XIndex(const std::vector<key_t> &keys, const std::vector<val_t> &vals,
         size_t worker_num, size_t bg_n);
  ~XIndex();

  inline bool get(const key_t &key, val_t &val, const uint32_t worker_id);
  inline bool put(const key_t &key, const val_t &val, const uint32_t worker_id);
  inline bool remove(const key_t &key, const uint32_t worker_id);
  inline size_t scan(const key_t &begin, const size_t n,
                     std::vector<std::pair<key_t, val_t>> &result,
                     const uint32_t worker_id);
  size_t range_scan(const key_t &begin, const key_t &end,
                    std::vector<std::pair<key_t, val_t>> &result,
                    const uint32_t worker_id);
 private:
  void start_bg();
  void terminate_bg();

  // this function should periodically check and perform structure updates
  static void *background(void *this_);

  root_t *volatile root = nullptr;
  pthread_t bg_master;
  size_t bg_num;
  volatile bool bg_running = true;
};

}  // namespace xindex

#endif  // XINDEX_H
