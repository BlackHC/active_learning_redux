store = {}
store['timestamp']=1620294907
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=6']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=40
store['config']={'seed': 7, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.218398332595825})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.3073229789733887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3925657272338867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.694021224975586})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.0320759765625}
store['active_learning_steps'][0]['acquisition']={'indices': [52959, 33126, 36281, 25341, 14614, 48010, 2702, 51137, 56775, 12066, 50806, 47635, 9346, 22675, 10539, 48030, 20037, 56792, 12377, 55531], 'labels': [2, 9, 7, 8, 8, 7, 9, 5, 0, 8, 9, 8, 9, 3, 9, 9, 8, 9, 3, 5], 'scores': [1.0984459519386292, 1.084953784942627, 1.0841144919395447, 1.079862356185913, 1.0767791271209717, 1.0747407674789429, 1.0638667941093445, 1.0631585121154785, 1.0581330060958862, 1.0531412959098816, 1.0523045063018799, 1.050851583480835, 1.0507510304450989, 1.0473892092704773, 1.0446600914001465, 1.0441220998764038, 1.0434850454330444, 1.0432500839233398, 1.0427404642105103, 1.0416934490203857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.80595064163208})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9285224676132202})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.0874924659729004})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2085278034210205})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7157, 'crossentropy': 1.55635205078125}
store['active_learning_steps'][1]['acquisition']={'indices': [20077, 38404, 18972, 56509, 10916, 32531, 1239, 5730, 4651, 1987, 56444, 23279, 41421, 23776, 36789, 34381, 27082, 23441, 56362, 46329], 'labels': [2, 0, 2, 0, 0, 0, 8, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 0, 3], 'scores': [1.042066514492035, 1.0309818983078003, 1.0071868896484375, 1.000958502292633, 0.9991791248321533, 0.9980118274688721, 0.9950428009033203, 0.9928624629974365, 0.9876105785369873, 0.9799922704696655, 0.9749472737312317, 0.9748364090919495, 0.9739651679992676, 0.9737814664840698, 0.9731407165527344, 0.9721446633338928, 0.9681353569030762, 0.966493546962738, 0.9638336300849915, 0.9608154296875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6588391065597534})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.1206016540527344})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.0296566486358643})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3260655403137207})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6964, 'crossentropy': 1.588909375}
store['active_learning_steps'][2]['acquisition']={'indices': [11025, 4360, 9390, 14368, 45256, 42139, 20172, 32977, 40493, 9468, 42781, 25315, 25644, 42213, 16248, 22824, 31094, 1423, 22091, 41295], 'labels': [5, 6, 9, 5, 5, 4, 4, 6, 4, 6, 4, 5, 4, 4, 7, 9, 9, 0, 6, 9], 'scores': [1.0403292179107666, 0.984020471572876, 0.9805392026901245, 0.9731771349906921, 0.9717646241188049, 0.9696708917617798, 0.9691186547279358, 0.9686159491539001, 0.9680243730545044, 0.9672642350196838, 0.9667611122131348, 0.9654093980789185, 0.9653646349906921, 0.9584280252456665, 0.9518181681632996, 0.9510973691940308, 0.9489147663116455, 0.9442969560623169, 0.94405597448349, 0.9401020407676697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2482190132141113})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6228435039520264})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.6482813358306885})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.6238083839416504})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7373, 'crossentropy': 1.23900625}
store['active_learning_steps'][3]['acquisition']={'indices': [10210, 39010, 32022, 41301, 38512, 49117, 36758, 11500, 20996, 5448, 23877, 33798, 36427, 32738, 15261, 35128, 50796, 33196, 29298, 44212], 'labels': [3, 7, 2, 2, 5, 3, 7, 5, 7, 7, 3, 7, 3, 7, 3, 2, 7, 7, 7, 7], 'scores': [0.8397234678268433, 0.8382778167724609, 0.8344500064849854, 0.8285799026489258, 0.8275793790817261, 0.8274800777435303, 0.8267802000045776, 0.8228863477706909, 0.8190764784812927, 0.8158859014511108, 0.812820553779602, 0.8115531206130981, 0.8105576634407043, 0.8082940578460693, 0.8081087470054626, 0.8059831857681274, 0.8043873310089111, 0.8029374480247498, 0.8012405633926392, 0.7988314628601074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.2029433250427246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.369401454925537})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.5357260704040527})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3896125555038452})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7342, 'crossentropy': 1.192500390625}
store['active_learning_steps'][4]['acquisition']={'indices': [49354, 58560, 33401, 3791, 53170, 43610, 34771, 55496, 27429, 8680, 51627, 51415, 9727, 19985, 13816, 3524, 17756, 16749, 16286, 47685], 'labels': [0, 0, 6, 2, 8, 0, 0, 9, 0, 8, 0, 0, 2, 0, 0, 6, 8, 0, 0, 2], 'scores': [0.869568943977356, 0.8493384718894958, 0.814720630645752, 0.8096327185630798, 0.809237003326416, 0.8087071776390076, 0.8043234348297119, 0.8009745478630066, 0.7982146739959717, 0.798197329044342, 0.7979175448417664, 0.7974775433540344, 0.7955422401428223, 0.7952497601509094, 0.795009970664978, 0.7940170764923096, 0.7924056053161621, 0.7889004945755005, 0.7849968075752258, 0.7809885740280151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2346248626708984})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1748536825180054})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.3120300769805908})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3857066631317139})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.488145112991333})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8168, 'crossentropy': 0.983310546875}
store['active_learning_steps'][5]['acquisition']={'indices': [40905, 12181, 34899, 32523, 49199, 20989, 38698, 1257, 25004, 35401, 27125, 4646, 41907, 18003, 47741, 14193, 47132, 8534, 49537, 14405], 'labels': [5, 5, 7, 2, 0, 3, 5, 6, 2, 3, 4, 2, 0, 2, 5, 4, 2, 4, 2, 6], 'scores': [0.9853388071060181, 0.9389753341674805, 0.9224568009376526, 0.9013586640357971, 0.9011048078536987, 0.9004939198493958, 0.8976696729660034, 0.896293044090271, 0.8959284722805023, 0.8956307172775269, 0.8940069675445557, 0.8922315835952759, 0.8912251591682434, 0.8886224627494812, 0.8874492645263672, 0.8864738345146179, 0.8827232122421265, 0.8731346130371094, 0.8729755282402039, 0.8715364933013916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1259524822235107})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8555693626403809})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8212728500366211})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1119654178619385})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0781651735305786})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0860978364944458})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8682, 'crossentropy': 0.75209091796875}
store['active_learning_steps'][6]['acquisition']={'indices': [14125, 14121, 50576, 38052, 12196, 51544, 42828, 45073, 14063, 19597, 7033, 39518, 5600, 7264, 26966, 24927, 34819, 54556, 25318, 42141], 'labels': [2, 2, 2, 4, 2, 1, 7, 2, 2, 9, 7, 2, 6, 9, 7, 9, 8, 2, 2, 5], 'scores': [1.0795405507087708, 1.0654021501541138, 1.0317081212997437, 0.989030122756958, 0.9862605929374695, 0.9763455390930176, 0.969168484210968, 0.9679363965988159, 0.9663515686988831, 0.963975191116333, 0.9568355083465576, 0.9536972045898438, 0.9485464692115784, 0.9461113214492798, 0.9416597485542297, 0.9414083957672119, 0.9352354407310486, 0.9346897006034851, 0.9316357374191284, 0.9307714104652405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1481131315231323})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8413857221603394})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8229546546936035})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.833553671836853})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9297623634338379})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9053629040718079})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8638, 'crossentropy': 0.7709634765625}
store['active_learning_steps'][7]['acquisition']={'indices': [42746, 20098, 4829, 25180, 60, 12986, 50370, 12985, 1573, 25960, 12332, 13520, 38716, 35946, 52514, 18324, 27473, 42112, 5045, 46333], 'labels': [2, 4, 4, 4, 4, 5, 7, 2, 2, 4, 4, 4, 4, 4, 6, 0, 4, 8, 9, 4], 'scores': [1.0378020405769348, 0.937188982963562, 0.9302261471748352, 0.9012552499771118, 0.9010027647018433, 0.8956736326217651, 0.8938775062561035, 0.8937590718269348, 0.8862398862838745, 0.8829577565193176, 0.8819223642349243, 0.8780203461647034, 0.8680949807167053, 0.8651579022407532, 0.8635085225105286, 0.8627362847328186, 0.8623154759407043, 0.8571363091468811, 0.8530691266059875, 0.8479243516921997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0225565433502197})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7646259069442749})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7499680519104004})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7538025379180908})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8903563022613525})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8055473566055298})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8736, 'crossentropy': 0.705793603515625}
store['active_learning_steps'][8]['acquisition']={'indices': [36744, 17404, 49824, 13652, 19586, 28930, 16190, 32047, 6182, 57342, 18654, 28512, 59368, 14394, 13969, 11202, 16488, 33358, 44732, 21946], 'labels': [1, 3, 8, 9, 9, 7, 3, 9, 3, 2, 4, 5, 5, 3, 3, 9, 9, 9, 6, 3], 'scores': [0.9148277640342712, 0.9057032465934753, 0.901138961315155, 0.9004470705986023, 0.8967254757881165, 0.894456148147583, 0.8904442191123962, 0.8868284821510315, 0.8814743161201477, 0.8778420090675354, 0.8687558174133301, 0.8608533143997192, 0.8598346710205078, 0.8592420816421509, 0.8588665127754211, 0.8526360392570496, 0.8519555330276489, 0.8510259985923767, 0.8509463667869568, 0.8497697114944458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9936953783035278})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8094525933265686})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6376851797103882})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7236634492874146})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8172661066055298})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7149169445037842})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.6168580078125}
store['active_learning_steps'][9]['acquisition']={'indices': [33505, 52697, 1075, 26733, 9180, 1127, 59314, 37016, 37469, 42703, 28199, 5842, 8932, 24424, 207, 34597, 58249, 31794, 57270, 34551], 'labels': [2, 3, 7, 2, 3, 7, 9, 5, 2, 0, 3, 1, 0, 1, 3, 3, 3, 2, 2, 3], 'scores': [0.8401610255241394, 0.8291205167770386, 0.8256297707557678, 0.8171173334121704, 0.8127192854881287, 0.8125177621841431, 0.8118770122528076, 0.809136152267456, 0.8041616678237915, 0.8040728569030762, 0.7960169911384583, 0.7947887182235718, 0.7937074899673462, 0.7869855165481567, 0.786578357219696, 0.7838954925537109, 0.7811753153800964, 0.7784801125526428, 0.7765055298805237, 0.7763038873672485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.10922110080719})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6959047317504883})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6052210330963135})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5808548927307129})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.702299952507019})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7722240090370178})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.715724766254425})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.578695263671875}
store['active_learning_steps'][10]['acquisition']={'indices': [22272, 1674, 3762, 24426, 35326, 52889, 11569, 33812, 33162, 3056, 37758, 7886, 32339, 50736, 53211, 14210, 43212, 22098, 4418, 59574], 'labels': [5, 9, 8, 5, 5, -1, 5, 6, 8, 4, 0, 9, 3, -1, -1, -1, 5, -1, 3, 5], 'scores': [0.9438925981521606, 0.9339678287506104, 0.924367368221283, 0.9210377335548401, 0.9156063199043274, 0.8973888158798218, 0.8972113132476807, 0.8968093693256378, 0.8963205814361572, 0.8834450244903564, 0.8726186156272888, 0.8725001811981201, 0.8719006180763245, 0.8652341961860657, 0.8582710027694702, 0.8579461574554443, 0.8562569618225098, 0.8548260927200317, 0.8536562919616699, 0.8525048494338989]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.1594982147216797})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8608431816101074})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7545705437660217})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7873910069465637})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8208357095718384})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7876395583152771})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8782, 'crossentropy': 0.6928826171875}
store['active_learning_steps'][11]['acquisition']={'indices': [59681, 31301, 7549, 51464, 21700, 18598, 40595, 19396, 53106, 59294, 30444, 7593, 492, 8704, 55483, 52049, 20169, 8771, 16019, 16084], 'labels': [0, 5, 6, 0, 7, 9, 8, 5, 6, 8, 6, 6, 1, 1, 6, 6, 4, 3, 3, 5], 'scores': [0.8902965784072876, 0.8498873710632324, 0.8492685556411743, 0.8374829292297363, 0.8354864120483398, 0.8337406516075134, 0.8315783739089966, 0.8311097621917725, 0.8272649049758911, 0.8270912170410156, 0.8252589106559753, 0.8245252370834351, 0.8206114172935486, 0.8179080486297607, 0.8177124261856079, 0.8173103332519531, 0.8162434697151184, 0.8150737285614014, 0.8114813566207886, 0.8088691234588623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1440625190734863})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6370530128479004})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5504722595214844})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5232930779457092})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5741579532623291})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5032860040664673})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.596262514591217})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5863679647445679})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5566269159317017})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.460831494140625}
store['active_learning_steps'][12]['acquisition']={'indices': [55778, 24404, 13942, 39561, 48916, 39355, 54196, 30763, 5155, 26358, 4036, 5474, 47626, 32863, 49252, 9687, 9340, 37465, 56512, 2548], 'labels': [-1, -1, 4, 2, -1, 8, -1, -1, 4, 3, -1, 8, -1, -1, 6, 0, 5, 5, -1, 4], 'scores': [1.0309295654296875, 1.0160375237464905, 0.9901772141456604, 0.9855828285217285, 0.9851405024528503, 0.9821351766586304, 0.9735771417617798, 0.97232586145401, 0.9697889685630798, 0.9683318138122559, 0.9675565958023071, 0.9664824604988098, 0.9663106203079224, 0.9576399326324463, 0.9546470046043396, 0.9517217874526978, 0.9460517466068268, 0.9420371055603027, 0.9355228543281555, 0.9307525455951691]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1354084014892578})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6079721450805664})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.576497495174408})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48183393478393555})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5207436680793762})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5488293170928955})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5495622158050537})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.452654248046875}
store['active_learning_steps'][13]['acquisition']={'indices': [38613, 34847, 39208, 54986, 31339, 52086, 32173, 52169, 6418, 14715, 8668, 44255, 47597, 25624, 48842, 33953, 36417, 35864, 7949, 15754], 'labels': [8, 0, 5, -1, 6, 5, 7, 2, 5, 4, 5, 6, 8, -1, 8, -1, 6, 5, -1, -1], 'scores': [0.9279417991638184, 0.8955544233322144, 0.8900356292724609, 0.8872032165527344, 0.877737820148468, 0.871852695941925, 0.866002082824707, 0.8625016808509827, 0.8618127703666687, 0.8581394553184509, 0.8535826802253723, 0.8515704274177551, 0.8510247468948364, 0.8496564626693726, 0.8492217063903809, 0.8449229598045349, 0.8439657688140869, 0.8436901569366455, 0.8435996770858765, 0.8434991240501404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0712673664093018})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6285042762756348})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4957698583602905})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5055065155029297})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5063654184341431})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4673547148704529})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4507787227630615})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5317707061767578})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48026150465011597})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.502413272857666})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.444916259765625}
store['active_learning_steps'][14]['acquisition']={'indices': [31014, 37161, 49890, 2375, 15423, 1682, 6050, 37048, 32449, 17895, 16983, 5440, 14309, 6443, 19058, 44013, 37881, 15771, 59658, 52889], 'labels': [8, 3, 5, 1, 1, 0, 7, 9, 1, 2, 1, -1, 1, 1, 1, 4, 1, 5, 1, -1], 'scores': [1.0365904569625854, 1.0220481753349304, 0.9965969324111938, 0.9728183746337891, 0.9654925465583801, 0.9653561115264893, 0.9608482122421265, 0.9580920934677124, 0.9541016817092896, 0.9535266160964966, 0.9438931941986084, 0.9397894144058228, 0.9395152926445007, 0.9369363784790039, 0.9366377592086792, 0.9356265962123871, 0.9355093240737915, 0.9352616667747498, 0.9347403645515442, 0.9338849782943726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9375489950180054})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5149116516113281})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5038349032402039})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5307303667068481})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49750572443008423})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.510874330997467})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5246512293815613})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5037987232208252})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.445023095703125}
store['active_learning_steps'][15]['acquisition']={'indices': [38391, 39585, 45026, 43745, 29711, 1160, 11292, 49889, 25043, 18239, 17079, 52671, 57714, 48824, 45516, 31313, 14619, 49502, 7924, 30173], 'labels': [8, 8, 8, 8, 8, 4, 1, 0, 8, 8, 6, 8, 1, 8, 1, 8, 3, 8, 8, 8], 'scores': [0.9802489280700684, 0.9505876302719116, 0.9426870346069336, 0.9423636794090271, 0.9389007687568665, 0.9376771450042725, 0.9285699725151062, 0.922503650188446, 0.9123166799545288, 0.9116511940956116, 0.9095770716667175, 0.9078771471977234, 0.9066904187202454, 0.9021661877632141, 0.898726224899292, 0.8962289094924927, 0.8934804201126099, 0.8914167284965515, 0.8898649215698242, 0.8895825147628784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.307770013809204})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6387642621994019})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4900094270706177})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44383472204208374})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4425002336502075})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4388182759284973})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49025288224220276})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4748152196407318})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42098236083984375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42712318897247314})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4181755781173706})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4292972981929779})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3969433009624481})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46459072828292847})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4891166090965271})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47407957911491394})
store['active_learning_steps'][16]['training']['best_epoch']=13
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9536, 'crossentropy': 0.4011431640625}
store['active_learning_steps'][16]['acquisition']={'indices': [37078, 51863, 3598, 20333, 36818, 32880, 21896, 5165, 52123, 36401, 53872, 11745, 3355, 23539, 644, 43045, 11550, 22437, 13971, 52801], 'labels': [8, 9, 9, 9, 7, 0, 8, 9, 9, 2, 8, 9, 9, 9, 7, -1, 9, 9, 9, 2], 'scores': [1.151501476764679, 1.1439381837844849, 1.1412511467933655, 1.121955156326294, 1.1129297614097595, 1.1012247204780579, 1.0981457829475403, 1.0749569535255432, 1.0674222707748413, 1.0646756291389465, 1.0634323358535767, 1.0599005222320557, 1.0583721995353699, 1.0575165748596191, 1.0549072623252869, 1.0504692792892456, 1.049913465976715, 1.0447862148284912, 1.0435671210289001, 1.0426210463047028]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0199248790740967})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6682561635971069})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46218132972717285})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38540732860565186})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41766637563705444})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3506008982658386})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33812159299850464})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41008925437927246})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36990320682525635})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39941516518592834})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9528, 'crossentropy': 0.3502932373046875}
store['active_learning_steps'][17]['acquisition']={'indices': [8447, 36072, 34188, 36268, 36078, 56414, 49826, 7322, 50317, 15848, 21390, 50308, 12702, 11446, 57728, 1559, 13714, 44385, 53990, 48038], 'labels': [3, 2, 3, 5, 3, -1, 3, 3, 3, 3, 3, 3, 3, -1, 9, 3, 4, -1, -1, 3], 'scores': [1.0365440845489502, 0.9816479682922363, 0.9439515471458435, 0.932392418384552, 0.9225553870201111, 0.9131312370300293, 0.9075011610984802, 0.9033646583557129, 0.8972580432891846, 0.8939102292060852, 0.89174884557724, 0.88987997174263, 0.8857263326644897, 0.882567286491394, 0.8800932168960571, 0.8746775388717651, 0.8732909560203552, 0.8731927871704102, 0.8716715574264526, 0.8690865635871887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1359224319458008})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4852520525455475})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.433013916015625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3752923309803009})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34125658869743347})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2949512004852295})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3466793894767761})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3880213499069214})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3379100263118744})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.3382283203125}
store['active_learning_steps'][18]['acquisition']={'indices': [57507, 24479, 59747, 34828, 14881, 39151, 40624, 33301, 19663, 25624, 29501, 1143, 23540, 12321, 54885, 42317, 14152, 18288, 8761, 31433], 'labels': [0, 8, 5, -1, 2, 4, -1, -1, -1, -1, -1, 2, -1, 0, 6, 5, 7, -1, 8, -1], 'scores': [1.0114174485206604, 0.9763877391815186, 0.9695593118667603, 0.9654079079627991, 0.9507518410682678, 0.9302871823310852, 0.9291068315505981, 0.9259870052337646, 0.923613429069519, 0.9174113273620605, 0.9138678312301636, 0.910590410232544, 0.9102665185928345, 0.9078954458236694, 0.9078683853149414, 0.9050394296646118, 0.903364360332489, 0.898932695388794, 0.8956009745597839, 0.895441472530365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.115015983581543})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5672330856323242})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43951982259750366})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37101826071739197})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3582964539527893})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3269459903240204})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3702906370162964})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37709420919418335})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37373489141464233})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.3470262939453125}
store['active_learning_steps'][19]['acquisition']={'indices': [24278, 32507, 12211, 19507, 13259, 3010, 45143, 34080, 19566, 48360, 42673, 45185, 59731, 26850, 14765, 15434, 18493, 50426, 2803, 27358], 'labels': [3, 5, 3, 1, 1, 7, 7, 1, -1, 3, 1, 7, 5, 2, 3, 2, 1, 7, 3, 8], 'scores': [0.908972978591919, 0.9065672159194946, 0.8818581700325012, 0.8732224106788635, 0.8702646493911743, 0.8533428311347961, 0.8529472947120667, 0.8499352931976318, 0.8438465595245361, 0.8427774906158447, 0.8353734612464905, 0.833961546421051, 0.8309404850006104, 0.8257303237915039, 0.8218849897384644, 0.821840226650238, 0.820896327495575, 0.8199380040168762, 0.8171579241752625, 0.8145835399627686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.105311393737793})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.580926775932312})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47988927364349365})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.357869952917099})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3881993293762207})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33402520418167114})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39777591824531555})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33851754665374756})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34899887442588806})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.3201220947265625}
store['active_learning_steps'][20]['acquisition']={'indices': [14201, 45972, 31757, 47036, 35406, 12392, 32427, 14643, 7308, 32776, 24197, 21636, 34328, 17603, 25300, 8458, 1596, 40334, 20206, 9118], 'labels': [7, 2, 2, 2, 5, 3, 0, 7, 8, 4, -1, 2, 8, 0, 7, 4, -1, 4, 7, 9], 'scores': [0.8921239376068115, 0.8790633678436279, 0.8777280449867249, 0.8755506277084351, 0.8725103139877319, 0.8594251871109009, 0.8511786460876465, 0.8494466543197632, 0.8471391201019287, 0.8435048460960388, 0.8390167951583862, 0.8322141766548157, 0.8289760947227478, 0.8284984827041626, 0.827279269695282, 0.8245919942855835, 0.8219941854476929, 0.8218569755554199, 0.8215891122817993, 0.8213194012641907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2077538967132568})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7004461884498596})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44983261823654175})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4151930809020996})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37626293301582336})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35238873958587646})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37392544746398926})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36854803562164307})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3646453619003296})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.315402685546875}
store['active_learning_steps'][21]['acquisition']={'indices': [46368, 52582, 55128, 47626, 22561, 42673, 4822, 26568, 42428, 23967, 33150, 11572, 13149, 43950, 52590, 32064, 43532, 54401, 50517, 6011], 'labels': [8, 2, 8, -1, 6, -1, 4, -1, 5, -1, 8, 5, 7, 9, -1, -1, 8, -1, 4, -1], 'scores': [0.9500834345817566, 0.9272353053092957, 0.9028288125991821, 0.8903199434280396, 0.8814858794212341, 0.8808143138885498, 0.8660272359848022, 0.8592902421951294, 0.8536691665649414, 0.8520246148109436, 0.8412727117538452, 0.841245710849762, 0.828311026096344, 0.8212773203849792, 0.8181756734848022, 0.8181298971176147, 0.8170345425605774, 0.814375638961792, 0.813594788312912, 0.813331127166748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1534755229949951})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5803993940353394})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45139896869659424})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41907429695129395})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34422969818115234})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3889482915401459})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3640485405921936})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33042842149734497})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3402252197265625})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3516616225242615})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3480309545993805})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.3000656494140625}
store['active_learning_steps'][22]['acquisition']={'indices': [10181, 57972, 15948, 16731, 1814, 7768, 53990, 17494, 33301, 34828, 52889, 21601, 27637, 49573, 49493, 48824, 14385, 6903, 46734, 39480], 'labels': [-1, 4, 2, -1, 4, 8, -1, 5, -1, -1, -1, 1, -1, 2, 8, -1, 8, 6, 4, 9], 'scores': [0.9527567625045776, 0.9361827373504639, 0.9311934113502502, 0.9277842044830322, 0.9052757024765015, 0.8950968384742737, 0.8857787251472473, 0.8842709064483643, 0.8822863101959229, 0.8819665312767029, 0.8817236423492432, 0.881719708442688, 0.8790262341499329, 0.8788264393806458, 0.8774946331977844, 0.8746882081031799, 0.8738901019096375, 0.868362545967102, 0.8669180870056152, 0.8656584024429321]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.192757248878479})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.710228681564331})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4539799094200134})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3398439288139343})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2915739417076111})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3480270504951477})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30023109912872314})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3034278154373169})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.2998061767578125}
store['active_learning_steps'][23]['acquisition']={'indices': [32323, 50930, 18130, 40466, 5175, 52889, 53054, 28368, 53844, 33338, 24589, 39405, 22495, 22083, 46021, 31738, 42384, 56006, 11708, 54954], 'labels': [5, 0, 8, 8, 4, -1, -1, 9, 5, 8, 8, 5, 4, 2, 9, 8, 8, 3, 3, 8], 'scores': [0.9263021945953369, 0.8523038625717163, 0.8268222808837891, 0.8232795596122742, 0.8055277466773987, 0.7848443984985352, 0.7833985090255737, 0.7823039293289185, 0.7818600535392761, 0.7811345458030701, 0.7789924740791321, 0.7773265838623047, 0.7731855511665344, 0.7656235694885254, 0.7591779232025146, 0.7563726305961609, 0.7559660077095032, 0.7554033398628235, 0.7543272376060486, 0.7506448030471802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.193993091583252})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6175066232681274})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5074610710144043})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44359487295150757})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3670917749404907})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36720937490463257})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37065643072128296})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31971102952957153})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3671422004699707})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39482319355010986})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32185617089271545})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9616, 'crossentropy': 0.31304638671875}
store['active_learning_steps'][24]['acquisition']={'indices': [44753, 47690, 2118, 59081, 391, 55790, 30751, 20792, 52462, 49515, 39316, 34829, 15779, 23956, 23540, 20050, 41156, 5430, 20005, 8883], 'labels': [5, 0, 7, -1, 2, 8, 0, 9, 9, 2, 7, 5, 0, 4, -1, 9, 0, 8, 6, 2], 'scores': [0.9021750092506409, 0.891559898853302, 0.8702143132686615, 0.8632009029388428, 0.8567810654640198, 0.8530079126358032, 0.846581757068634, 0.844005286693573, 0.8440026640892029, 0.8438498377799988, 0.8400285840034485, 0.8365827798843384, 0.8335387706756592, 0.8329299092292786, 0.8327740430831909, 0.832501232624054, 0.830610990524292, 0.8301761150360107, 0.8290204405784607, 0.8276567459106445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2128156423568726})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7340213060379028})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45921260118484497})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35567736625671387})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3823707401752472})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32158172130584717})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3204728364944458})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3053419291973114})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3216560482978821})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32932984828948975})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32136058807373047})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.3094417724609375}
