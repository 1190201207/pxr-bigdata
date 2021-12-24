

#include <memory>
#include <vector>

#include "xindex_group.h"

#if !defined(XINDEX_ROOT_H)
#define XINDEX_ROOT_H

namespace xindex {
/*
 * HRoot
 */
template <class key_t, class val_t>
class HRoot {
  typedef LinearModel<key_t> linear_model_t;
  typedef HGroup<key_t, val_t> group_t;

  template <class key_tt, class val_tt>
  friend class XIndex;

 public:
  ~HRoot();
  void init(const std::vector<key_t> &keys, const std::vector<val_t> &vals);

  inline result_t get(const key_t &key, val_t &val);
  inline result_t put(const key_t &key, const val_t &val);
  inline result_t remove(const key_t &key);

  static void *do_maintenance(void *args);

 private:
  void train_rmi(const std::vector<key_t> &keys);
  size_t locate_group_idx(const key_t &key);
  inline group_t *locate_group(const key_t &key);
  double re_init(const std::vector<key_t> &keys, const std::vector<val_t> &vals,
                 size_t current_group_n);

  linear_model_t model_t;
  std::unique_ptr<group_t *volatile[]> groups;
  size_t group_n = 100;
  size_t table_size;
};

}  // namespace xindex

#endif  // XINDEX_ROOT_H
